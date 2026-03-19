from flask import Blueprint, jsonify, request
from database.database import get_db_connection
from utils.utils import current_time_date, upload_image, send_mail, current_date, current_time, check_image_size, upload_resume
from security.jwt_utils import token_required, role_required
from logger_config.loger_config import get_logger

seeker_bp = Blueprint('seeker', __name__)

logger = get_logger()

@seeker_bp.route('/per_info', methods=['POST'])
@token_required
@role_required("seeker")
def seeker_personal_info():
    if getattr(request, "status", None) != "verified":
        return jsonify({"error": "ACCOUNT_NOT_VERIFIED"}), 403

    data = request.get_json(silent=True)
    print(data)
    if not data:
        return jsonify({"message": "All data required"}), 400
    
    required_fields = ["dob", "gender", "country", "state", "city", "pincode", "about"]
    missing = [f for f in required_fields if f not in data or not data[f]]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    name = data.get("name", "").strip()
    dob = data.get("dob", "").strip()
    gender = data.get("gender", "").strip()
    country = data.get("country", "").strip()
    state = data.get("state", "").strip()
    city = data.get("city", "").strip()
    pincode = data.get("pincode", "").strip()
    photo = data.get("photo", "").strip()
    about = data.get("about", "").strip()

    #full name
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT full_name FROM users WHERE id=%s", (request.user_id,))
        user = cur.fetchone()
        full_name = user["full_name"] if user else ""
    except Exception as e:
        return jsonify({"error": f"error: {str(e)}"})
    finally:
        cur.close()
        db.close()

    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)


        cur.execute("SELECT * FROM seeker_personal_info WHERE seeker_id=%s",(request.user_id,))
        res = cur.fetchone()

        if res:
            # if not res["photo"]:
            if photo:
                if not check_image_size(photo):
                    return jsonify({"message": "Photo is too large must be 3MB"}), 400
                p_url = upload_image(photo)
            else:
                p_url = res["photo"]
            # else:
            #     p_url = res["photo"]
            cur.execute(
                """
                UPDATE seeker_personal_info
                SET
                    name = %s,
                    date_of_birth = %s,
                    gender = %s,
                    country = %s,
                    state = %s,
                    city = %s,
                    pincode = %s,
                    photo = %s,
                    about = %s,
                    registered_on = %s
                WHERE seeker_id = %s
                """,
                (
                    name,
                    dob,
                    gender,
                    country,
                    state,
                    city,
                    pincode,
                    p_url,
                    about,
                    current_time_date(),
                    request.user_id
                )
            )

            db.commit()
            return jsonify({"message": "Profile updated successfully"}), 200

        else:
            if photo:
                if not check_image_size(photo):
                    return jsonify({"message": "Photo is too large must be 3MB"}), 400
                p_url = upload_image(photo)
            else:
                p_url = "https://img.freepik.com/free-icon/user_318-388892.jpg"
            cur.execute(
                "INSERT INTO seeker_personal_info(seeker_id, name, date_of_birth, gender, country, state, city, pincode, photo, about, registered_on) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (request.user_id, full_name, dob, gender, country, state, city, pincode, p_url, about, current_time_date())
            )

            db.commit()
            return jsonify({"message": "Profile updated successfully"}), 200

    except Exception as e:
        db.rollback()
        return jsonify({"error": f"Error: {e}"}), 500

    finally:
        if db and db.is_connected():
            cur.close()
            db.close()


@seeker_bp.route('/prof_info', methods=['POST'])
@token_required
@role_required("seeker")
def seeker_professional_info():


    if getattr(request, "status", None) != "verified":
        return jsonify({"error": "ACCOUNT_NOT_VERIFIED"}), 403


    data = request.get_json(silent=True)
    print(data)
    if not data:
        return jsonify({"message": "All data required"}), 400
    
    required_fields = ["employment_status", "preferred_location", "open_for"]
    missing = [f for f in required_fields if f not in data or not data[f]]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    employment_status = data.get("employment_status", "unemployed")
    current_role = data.get("current_role")
    experience_years = data.get("experience_years")
    preferred_location = data.get("preferred_location")
    open_for = data.get("open_for", "None")

    try:
        experience_years = float(data.get("experience_years", 0))
    except ValueError:
        return jsonify({"message": "Invalid experience years"}), 400
    
    if employment_status == "unemployed" or employment_status == "fresher":
        current_role = None
        experience_years = 0

    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM seeker_professional_info WHERE seeker_id=%s",(request.user_id,))
        res = cur.fetchone()

        if res:
                
                cur.execute("UPDATE seeker_professional_info SET employment_status = %s,current_role = %s,experience_years = %s,preferred_location = %s,open_for = %s WHERE seeker_id = %s",
                            (employment_status,current_role,experience_years,preferred_location,open_for,request.user_id))

                db.commit()
                return jsonify({"message": "Details updated successfully"}), 200
        else:
                cur.execute( "INSERT INTO seeker_professional_info(seeker_id, employment_status, current_role, experience_years, preferred_location, open_for)" \
                            " VALUES (%s, %s, %s, %s, %s, %s)",
                            (request.user_id,employment_status,current_role,experience_years,preferred_location,open_for) )

                db.commit()
                return jsonify({"message": "Details updated successfully"}), 200

    except Exception as e:
        db.rollback()
        return jsonify({"error": f"Error: {e}"}), 500

    finally:
        if db and db.is_connected():
            cur.close()
            db.close()


# done ----------------------------
@seeker_bp.route('/acd_info', methods=['POST'])
@token_required
@role_required("seeker")
def seeker_academic_info():

    if getattr(request, "status", None) != "verified":
        return jsonify({"error": "ACCOUNT_NOT_VERIFIED"}), 403


    data = request.get_json(silent=True)
    print(data)
    if not data:
        return jsonify({"error": "INVALID_JSON"}), 400

    required = ["level", "institution_name", "start_year"]
    missing = [f for f in required if not data[f]]
    if missing:
        return jsonify({"error": "MISSING_FIELDS", "fields": missing}), 400

    level = data.get("level")
    institution = data.get("institution_name")
    start_year = int(data.get("start_year"))
    end_year = int(data.get("end_year"))
    is_current = data.get("is_current")
    current_year = data.get("current_year")

    if is_current == "yes":
        end_year = None
    else:
        current_year = None

    try:
        db = get_db_connection()
        cur = db.cursor()

        query = """
        INSERT INTO seeker_academic_info
            (seeker_id, level, institution_name, start_year, end_year, is_current, current_year)
        VALUES
            (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            institution_name = VALUES(institution_name),
            start_year = VALUES(start_year),
            end_year = VALUES(end_year),
            is_current = VALUES(is_current),
            current_year = VALUES(current_year)
        """

        cur.execute(query, (request.user_id, level, institution, start_year, end_year, is_current, current_year))

        db.commit()
        return jsonify({"message": "Academic info saved"}), 200

    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cur.close()
        db.close()

# done ---

@seeker_bp.route('/skill_info', methods=['POST'])
@token_required
@role_required("seeker")
def seeker_skill_info():

    if getattr(request, "status", None) != "verified":
        return jsonify({"error": "ACCOUNT_NOT_VERIFIED"}), 403


    data = request.get_json(silent=True)
    print(data)
    if not data:
        return jsonify({"message": "All data required"}), 400
    
    # check the missing value
    required_fields = ["skill", "proficiency"]
    missing = [f for f in required_fields if f not in data or not data[f]]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    skill = data.get("skill")
    proficiency = data.get("proficiency")
    
    if proficiency not in ["beginner", "intermediate", "expert"]:
        return jsonify({
            "error": "INVALID_PROFICIENCY",
            "message": "Proficiency must be one of: beginner, intermediate, or expert"
    }), 400

    try:
        db = get_db_connection()
        cur = db.cursor()

        query = """
        INSERT INTO seeker_skills
            (seeker_id, skill, proficiency)
            VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            proficiency = VALUES(proficiency)
        """

        cur.execute(query, (request.user_id, skill, proficiency))

        db.commit()
        return jsonify({"message": "skill info saved"}), 200

    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cur.close()
        db.close()


# send details-----------------------
@seeker_bp.route("/profile", methods=["GET"])
@token_required
@role_required("seeker")
def get_seeker_profile():


    seeker_id = request.user_id

    db = get_db_connection()
    cur = db.cursor(dictionary=True)

    try:
        cur.execute("""
            SELECT
                u.email,
                u.phone,
                u.visibility,

                sp.name,
                sp.date_of_birth,
                sp.gender,
                sp.country,
                sp.state,
                sp.city,
                sp.pincode,
                sp.photo,
                sp.about,

                pr.employment_status,
                pr.current_role,
                pr.experience_years,
                pr.preferred_location,
                pr.open_for

            FROM users u
            LEFT JOIN seeker_personal_info sp ON u.id = sp.seeker_id
            LEFT JOIN seeker_professional_info pr ON u.id = pr.seeker_id
            WHERE u.id = %s
        """, (seeker_id,))

        profile = cur.fetchone()
        if not profile:
            return jsonify({"error": "SEEKER_NOT_FOUND"}), 404

        cur.execute("""
            SELECT level, institution_name, start_year, end_year, is_current, current_year
            FROM seeker_academic_info
            WHERE seeker_id = %s
            ORDER BY start_year
        """, (seeker_id,))
        acd_info = cur.fetchall()
        if not acd_info:
            academics = None
        else:
            academics = acd_info

        cur.execute("""
            SELECT skill, proficiency
            FROM seeker_skills
            WHERE seeker_id = %s
        """, (seeker_id,))
        skill_info = cur.fetchall()
        if not skill_info:
            skills = None
        else:
            skills = skill_info

        return jsonify({
            "profile": profile,
            "academics": academics,
            "skills": skills
        }), 200

    finally:
        cur.close()
        db.close()

# ---done
@seeker_bp.route("/apply_on_job", methods=["POST"])
@token_required
@role_required("seeker")
def apply_on_job():
    if getattr(request, "status", None) != "verified":
        return jsonify({"error": "ACCOUNT_NOT_VERIFIED"}), 403
    
    data = request.get_json()

    if not data:
        return jsonify({"error": "no data present in tha data"})

    required_fields = ["job_id", "message", "resume"] #"resume"
    missing = [f for f in required_fields if f not in data or not data[f]]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400
    
    job_id = int(data.get("job_id"))
    message = data.get("message", "")
    resume = data.get("resume", "")

    print("job id", job_id)
    print("message", message)
    print("resume length:", len(resume))

    if not resume:
        resume_url = None
    else:
        if check_image_size(resume):
            resume_url = upload_resume(resume)
        else:
            return jsonify({"message": "Resume size is too large must be 3MB"}), 400
    


    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("SELECT status FROM jobs WHERE id=%s",(job_id,))
        re = cur.fetchone()
        if res["status"] != "open":
            return jsonify({"msg": "Not Allow for this job"}), 409
        
        cur.execute("SELECT * FROM job_applications WHERE job_id=%s AND job_seeker_id=%s",(job_id, request.user_id))
        res = cur.fetchone()
        if res:
            return jsonify({"message": "Already apply"}), 409
        
        cur.execute("INSERT INTO job_applications(job_id, job_seeker_id, message, resume, applied_at) VALUEs (%s, %s, %s, %s, %s)",
                    (job_id, request.user_id, message, resume_url, current_date()))
        
        cur.execute("UPDATE jobs SET number_of_applications = number_of_applications+1 WHERE id =%s",(job_id,))
        
        print("job id", job_id)
        print("message", message)
        print("resume length:", len(resume))
        print(resume_url)

        db.commit()
        return jsonify({"message": "Apply sucess full"}), 200


    except Exception as e:
        db.rollback()
        print("error in upload: ",str(e))
        return jsonify({"error": f"{str(e)}"})
    finally:
        print("complete...............🌿🌿🌿🌿")
        cur.close()
        db.close()





# delet skill
@seeker_bp.route('/delete_skill', methods=['DELETE'])
@token_required
@role_required("seeker")
def delete_skill():

    if getattr(request, "status", None) != "verified":
        return jsonify({"error": "ACCOUNT_NOT_VERIFIED"}), 403

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"message": "All data required"}), 400
    
    # check the missing value
    required_fields = ["id"]
    missing = [f for f in required_fields if f not in data or not data[f]]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    id = data.get("id")
    
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("DELETE FROM seeker_skills WHERE id=%s AND seeker_id=%s", (id, request.user_id))
        
        if cur.rowcount == 0:
            return jsonify({"error": "Skill not found"}), 404
        db.commit()
        return jsonify({"message": "Skill deleted"}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cur.close()
        db.close()




@seeker_bp.route("/job_openings", methods = ["GET"])
@token_required
@role_required("seeker")
def job_openings():

    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("SELECT id, title, employment_type, salary_max, number_of_applications FROM jobs WHERE status=%s",("open",))
        res = cur.fetchall()

        return jsonify({"jobs": res})

    except Exception as e:
        print("error", str(e))
        return jsonify({"error": str(e)})
    finally:
        cur.close()
        db.close()


