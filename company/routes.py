from utils.utils import current_time_date, upload_image, send_mail, current_date, check_image_size, analyze_resume_from_url
from security.jwt_utils import token_required, role_required
from database.database import get_db_connection
from logger_config.loger_config import get_logger
from flask import Blueprint, jsonify, request
import email_templates.templates
import base64

company_bp = Blueprint('company', __name__)

logger = get_logger()

# done -----------------------------
@company_bp.route('/company_info', methods=['POST'])
@token_required
@role_required("company")
def company_info():

    if getattr(request, "status", None) != "verified":
        return jsonify({"error": "ACCOUNT_NOT_VERIFIED"}), 403
    

    data = request.get_json(silent=True)
    print(data)
    if not data:
        return jsonify({"message": "All data required"}), 400
    
    required_fields = ["website", "company_type", "industry_type", "company_size", "state", "city", "pincode", "about"]
    missing = [f for f in required_fields if f not in data or not data[f]]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    # name = data.get("name", "").strip()
    website = data.get("website", "").strip()
    company_type = data.get("company_type", "").strip()
    industry_type = data.get("industry_type", "").strip()
    company_size = data.get("company_size", "").strip()
    state = data.get("state", "").strip()
    city = data.get("city", "").strip()
    pincode = int(data.get("pincode"))
    cin_number = data.get("cin_number", "").strip()
    gstin = data.get("gstin", "").strip()
    udyam_number = data.get("udyam_number", "").strip()
    incorporation_certificate = data.get("incorporation_certificate", "")
    logo = data.get("logo", "")
    about = data.get("about", "").strip()

    if company_type == "Startup":
        if not any([cin_number, gstin, udyam_number]):
            return jsonify({"message": "You must provide at least one of CIN, GSTIN, or UDYAM number."}), 400

    if company_type in ["Private Limited", "Public Limited", "Government", "LLP"]:
        if not all([cin_number, gstin]):
            return jsonify({"message": "You must provide both CIN and GSTIN."}), 400
        
        if not incorporation_certificate:
            return jsonify({"message": "You must provide incorporation certificate"}), 400
        

    
    if incorporation_certificate:
        try:
            incorporation_certificate_bytes = base64.b64decode(
                incorporation_certificate, validate=True
            )
        except Exception:
            return jsonify({"error": "INVALID_CERTIFICATE_BASE64"}), 400
    else:
        incorporation_certificate_bytes = None
        

    if not logo:
        logo_url = "https://img.icons8.com/?size=100&id=53426&format=png"
    else:
        if check_image_size(logo):
            logo_url = upload_image(logo)
        else:
            return jsonify({"message": "Logo is too large must be 3MB"}), 400
        
# pdf_base64 = base64.b64encode(
#     row["incorporation_certificate"]
# ).decode("utf-8") after retrive

    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("SELECT * FROM company_info WHERE company_id=%s",(request.user_id,))
        check = cur.fetchone()
        if check:
            return jsonify({"message": "you have already filled your details"})

        cur.execute("SELECT email, phone, full_name FROM users WHERE id=%s",(request.user_id,))
        res = cur.fetchone()

        cur.execute(
            "INSERT INTO company_info (company_id, name, email, contact_no, website, company_type, industry_type, company_size, "
            "state, city, pincode, cin_number, gstin, udyam_number, incorporation_certificate, logo, about, registered_on) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                request.user_id, res["full_name"], res["email"], res["phone"], website, company_type, industry_type, company_size,
                state, city, pincode, cin_number, gstin, udyam_number, incorporation_certificate_bytes, logo_url,  about, current_time_date()
            )
        )

        db.commit()
        response = email_templates.templates.company_details_uploaded()
        send_mail(response["subject"], response["body"], res["email"], "html")
        return jsonify({"message": "information saved wait for verification"}), 200

    except Exception as e:
        db.rollback()
        print(str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
        db.close()




# done -----------------------------
@company_bp.route('/post_job', methods=['POST'])
@token_required
@role_required("company")
def job_info():
    if getattr(request, "status", None) != "verified":
        return jsonify({"error": "ACCOUNT_NOT_VERIFIED"}), 403
    

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"message": "All data required"}), 400
    
    required_fields = ["title", "description", "skill_need", "employment_type", "experience_min", "salary_min", "salary_max", "location", "is_remote", "close_on"]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    title = data.get("title", "").strip()
    description = data.get("description", "").strip()
    skill_need = data.get("skill_need", "").strip()
    employment_type = data.get("employment_type", "").strip()
    try:
        experience_min = float(data.get("experience_min"))
        salary_min = int(data.get("salary_min"))
        salary_max = int(data.get("salary_max"))
    except (TypeError, ValueError):
        return jsonify({"error": "INVALID_NUMERIC_FIELDS"}), 400
    location = data.get("location", "").strip()
    is_remote = data.get("is_remote", "").strip()
    close_on = data.get("close_on", "").strip()

    if salary_min >= salary_max:
        return jsonify({"message": "invalid salary range"})

    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("SELECT verification_status FROM company_info WHERE company_id=%s",(request.user_id,))
        check = cur.fetchone()
        if not check or check["verification_status"] != "verified":
            return jsonify({"error": "COMPANY_NOT_VERIFIED"}), 403


        cur.execute(
            "INSERT INTO jobs (company_id, title, description, skill_need, employment_type, experience_min, salary_min, salary_max, "
            "location, is_remote, close_on, created_at) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                request.user_id, title, description, skill_need, employment_type, experience_min, salary_min, salary_max,
                location, is_remote, close_on, current_date()
            )
        )

        db.commit()
        return jsonify({"message": "details uploaded sucessfully"}), 200

    except Exception as e:
        db.rollback()
        print("error:===",str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
        db.close()

@company_bp.route('/profile', methods=['GET'])
@token_required
@role_required("company")
def view_company_info():
    if getattr(request, "status", None) != "verified":
        return jsonify({"error": "ACCOUNT_NOT_VERIFIED"}), 403

    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute(
            "SELECT * FROM company_info WHERE company_id = %s",
            (request.user_id,)
        )
        company_details = cur.fetchone()

        if not company_details:
            return jsonify({
                "error": "PROFILE_NOT_FOUND"
            }), 404

        return jsonify({
                "id": company_details["id"],
                "name": company_details["name"],
                "email": company_details["email"],
                "contact_no": company_details["contact_no"],
                "website": company_details["website"],
                "company_type": company_details["company_type"],
                "industry_type": company_details["industry_type"],
                "company_size": company_details["company_size"],
                "state": company_details["state"],
                "city": company_details["city"],
                "pincode": company_details["pincode"],
                "cin_number": company_details["cin_number"],
                "gstin": company_details["gstin"],
                "udyam_number": company_details["udyam_number"],
                "logo": company_details["logo"],
                "about": company_details["about"]
        }), 200

    except Exception:
        return jsonify({"error": "INTERNAL_SERVER_ERROR"}), 500

    finally:
        cur.close()
        db.close()




#analzee  aapplication resume :-
@company_bp.route("/analyze_resume/<int:application_id>", methods = ["GET"])
@token_required
@role_required("company")
def analyze_resume(application_id):
    if getattr(request, "status", None) != "verified":
        return jsonify({"error": "ACCOUNT_NOT_VERIFIED"}), 403
    
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("SELECT * FROM job_applications WHERE id=%s",(application_id,))
        res = cur.fetchone()

        if not res:
            return jsonify({"msg": "application not found"})
        
        cur.execute("SELECT company_id FROM jobs WHERE id=%s",(int(res["job_id"]),))
        r = cur.fetchone()
        if r["company_id"] != request.user_id:
            return jsonify({"msg": "not allow"}), 403
        

        if res["application_status"] == "rejected":
            return jsonify({"msg": "the application is rejected"}), 400
        
        ressult = analyze_resume_from_url(res["resume"])

        return jsonify({"result": ressult})

    except Exception as e:
        print("error: ", str(e))
        return jsonify({"error": "Error happen"})
    finally:
        cur.close()
        db.close()


@company_bp.route("/approve_application/<int:application_id>", methods = ["GET"])
@token_required
@role_required("company")
def approve_application(application_id):

    if getattr(request, "status", None) != "verified":
        return jsonify({"error": "ACCOUNT_NOT_VERIFIED"}), 403
    
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("SELECT application_status, job_id FROM job_applications WHERE id=%s",(application_id,))
        res = cur.fetchone()

        if not res:
            return jsonify({"error": "APPLICATION_NOT_FOUND"}), 404
        
        if res["application_status"] == "applied":
            return jsonify({"msg": "Action Not Allow"}), 403
        
        cur.execute("UPDATE job_applications SET application_status=%s WHERE id=%s",("shortlisted", application_id))
        cur.execute("UPDATE jobs SET number_of_applications = GREATEST(number_of_applications - 1, 0) WHERE id=%s",(res["job_id"],))
        db.commit()

        return jsonify({"msg": "Aproved Sucess full"}), 200

    except Exception as e:
        db.rollback()
        return jsonify({"error", "Error happen"})
    
    finally:
        cur.close()
        db.close()



@company_bp.route("/reject_application/<int:application_id>", methods = ["GET"])
@token_required
@role_required("company")
def reject_application(application_id):

    if getattr(request, "status", None) != "verified":
        return jsonify({"error": "ACCOUNT_NOT_VERIFIED"}), 403
    
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("SELECT application_status, job_id FROM job_applications WHERE id=%s",(application_id,))
        res = cur.fetchone()

        if not res:
            return jsonify({"error": "APPLICATION_NOT_FOUND"}), 404
        
        if res["application_status"] == "rejected":
            return jsonify({"msg": "Action Not Allow"}), 403
                
        cur.execute("UPDATE job_applications SET application_status=%s WHERE id=%s",("rejected", application_id))
        cur.execute("UPDATE jobs SET number_of_applications = GREATEST(number_of_applications - 1, 0) WHERE id=%s",(res["job_id"],))
        db.commit()

        return jsonify({"msg": "reject Sucess full"}), 200

    except Exception as e:
        db.rollback()
        return jsonify({"error", "Error happen"})
    
    finally:
        cur.close()
        db.close()


@company_bp.route("/company_jobs", methods = ["GET"])
@token_required
@role_required("company")
def company_jobs():
    company_id = int(request.user_id)

    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("SELECT title, number_of_applications, created_at, close_on FROM jobs WHERE company_id=%s, AND status=%s",(company_id, "open"))
        res = cur.fetchall()
        if res:
            return jsonify({"res": res})
        else:
            return jsonify({"res": "No Job Found"})
    except Exception as e:
        print("error:==", str(e))
        return jsonify({"err", "error happen"})
    finally:
        cur.close()
        db.close()

@company_bp.route("/applications/<int:application_id>", methods=["GET"])
@token_required
@role_required("company")
def applications(application_id):
    compny_id = request.user_id
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("""SELECT
                    u.full_name AS name,
                    u.email AS email,
                    u.""")

    except Exception as e:
        print("error: ===", str(e))
        return jsonify({"err": "Error happen"})
    finally:
        cur.close()
        db.close()