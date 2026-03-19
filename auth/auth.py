from flask import Blueprint, jsonify, redirect
from database.database import get_db_connection
from logger_config.loger_config import get_logger

auth_bp = Blueprint('auth', __name__)

logger = get_logger()

@auth_bp.route('/verify-email/<token>', methods=['GET'])
def email_verify(token):
    logger.info("email verify token generator")
    if not token:
        return jsonify({"message": "Invalid verification link"}), 400

    db = None
    cur = None

    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute(
            "SELECT id, status FROM users WHERE verification_token = %s",
            (token,)
        )
        user = cur.fetchone()

        if not user:
            return jsonify({"message": "Invalid or expired verification link"}), 400

        if user["status"] == "verified":
            return jsonify({"message": "Account already verified"}), 200

        cur.execute(
            "UPDATE users SET status=%s, verification_token=NULL WHERE id=%s",
            ("verified", user["id"])
        )
        db.commit()

        return redirect("https://verify-email-deepti.netlify.app/")

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        print("VERIFY EMAIL ERROR:", e)
        return jsonify({"message": "Server error"}), 500

    finally:
        if cur:
            cur.close()
        if db:
            db.close()
