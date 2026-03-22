from security.jwt_utils import token_required, role_required
from flask import Blueprint, request, jsonify
from database.database import get_db_connection
from logger_config.loger_config import get_logger
from utils.utils import current_time_date, send_mail
import email_templates.templates
import requests
from dotenv import load_dotenv
import os

admin_bp = Blueprint('admin', __name__)

logger = get_logger()



@admin_bp.route("/view_applied_company", methods = ["GET"])
@token_required
@role_required("admin")
def view_applied_company():
    try:
        db= get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT company_id, name, email FROM company_info where verification_status=%s", ("unverified",))
        res = cur.fetchall()

        if not res:
            return jsonify({"res": "no company avilable"})

        return jsonify({"res": res}), 200


    except Exception as e:
        logger.error(f"Error : {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
        db.close()

@admin_bp.route("/view_applied_company_details/<int:company_id>", methods = ["GET"])
@token_required
@role_required("admin")
def view_applied_company_details(company_id):
    try:
        db= get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM company_info where company_id=%s", (company_id,))
        res = cur.fetchall()

        if not res:
            return jsonify({"res": "no company avilable"})

        return jsonify({"res": res}), 200


    except Exception as e:
        logger.error(f"Error : {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()
        db.close()

@admin_bp.route("/aprove_company/<int:company_id>", methods = ["GET"])
@token_required
@role_required("admin")
def aprove_company(company_id):
    try:
        db= get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT verification_status, name, email FROM company_info where company_id=%s", (company_id,))
        res = cur.fetchone()

        if not res:
            return jsonify({"msg": "no company found"})
        
        if res["verification_status"] != "unverified":
            return jsonify({"msg": "action not allow"}), 401
        
        cur.execute("UPDATE company_info SET verification_status=%s WHERE company_id=%s",("verified", company_id))
        db.commit()

            # send alert in email
        try:
            response = email_templates.templates.company_approved(res["name"].split()[0], current_time_date())
            send_mail(response["subject"], response["body"], res["email"], "html")
        except Exception as e:
            logger.error(f"Email send error: {str(e)}")
            print("Email failed:", e)

        return jsonify({"msg": "Aproved Sucessful"})

    except Exception as e:
        db.rollback()
        logger.error(f"Error : {str(e)}")
    finally:
        cur.close()
        db.close()

@admin_bp.route("/reject_company/<int:company_id>", methods = ["POST"])
@token_required
@role_required("admin")
def reject_company(company_id):
    data = request.get_json(silent=True)
    print(data)

    # HARD validation
    if not data or not data.get("post_id"):
        return jsonify({"error": "post_id required"}), 400
    try:
            db= get_db_connection()
            cur = db.cursor(dictionary=True)
            cur.execute("SELECT verification_status, name, email FROM company_info where company_id=%s", (company_id,))
            res = cur.fetchone()

            if not res:
                return jsonify({"msg": "no company found"})
            
            if res["verification_status"] != "unverified":
                return jsonify({"msg": "action not allow"}), 401
            
            cur.execute("UPDATE company_info SET verification_status=%s WHERE company_id=%s",("rejected", company_id))
            db.commit()
            
                # send alert in email
            try:
                response = email_templates.templates.reject_company(res["name"].split()[0], current_time_date(), data["reason"])
                send_mail(response["subject"], response["body"], res["email"], "html")
            except Exception as e:
                logger.error(f"Email send error: {str(e)}")
                print("Email failed:", e)

            return jsonify({"msg": "Aproved Sucessful"})

    except Exception as e:
        db.rollback()
        logger.error(f"Error : {str(e)}")
    finally:
        cur.close()
        db.close()
