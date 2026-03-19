from utils.utils import current_time_date, send_mail, generate_url_code, verify_phone_number, validate_email_adress
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter.util import get_remote_address
from database.database import get_db_connection
from logger_config.loger_config import get_logger
from security.jwt_utils import token_required
from security.jwt_utils import generate_token
from flask import Flask, request, jsonify
from flask_limiter import Limiter
from mysql.connector import Error
import email_templates.templates
from dotenv import load_dotenv
# from datetime import datetime
from flask_cors import CORS
from waitress import serve
import requests
import uuid
import os

# -------------------- LOAD ENV --------------------
load_dotenv()


# -------------------- APP INIT --------------------
app = Flask(__name__)
CORS(app)


# -------------------- LOGER CONFIG --------------------
logger = get_logger()

# ------------------- BLUE PRINT REGISTRATIION --------------------------
from auth.auth import auth_bp
from seeker.routes import seeker_bp
from company.routes import company_bp
from content_post.routes import content_bp
from problam_practice.routes import problam_bp


app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(seeker_bp, url_prefix='/seeker')
app.register_blueprint(company_bp, url_prefix='/company')
app.register_blueprint(content_bp, url_prefix='/content')
app.register_blueprint(problam_bp, url_prefix='/problem')


# -------------------- RATE LIMITER --------------------
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
limiter.init_app(app)

# -------------------- SECURITY HEADERS --------------------
@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response



# ===================== LOGGING FOR FLASK DEBUGGING =====================

from colorama import Fore, Style, init
init(autoreset=True)

@app.before_request
def log_request():
    print(Fore.CYAN + f"\n[REQUEST] {request.method} {request.path} | IP: {request.remote_addr}")
    # print(Fore.CYAN+f"\n{request.method} {request.path}")


@app.after_request
def log_response(response):
    status_code = response.status_code

    if status_code >= 500:
        color = Fore.RED
    elif status_code >= 400:
        color = Fore.YELLOW
    else:
        color = Fore.GREEN

    print(color + f"\n[RESPONSE] {response.status} / {request.method} {request.path}" + Style.RESET_ALL)

    return response


@app.errorhandler(Exception)
def handle_error(e):
    print(Fore.RED + f"\nERROR: {str(e)}")
    return jsonify({"error": "Internal error"}), 500

#-------------------------- END-POINT SECTION START -------------------------------------------


# ---------------- HEALTH  ROUT FOE SERVER------------------------------------------------

@app.route("/health", methods=["GET"])
def test_db():
    logger.info("health cheeck")
    db = get_db_connection()
    if db and db.is_connected():
        try:
            print("dsjkfhjkdhfjkhsdgfjksd")
            cursor = db.cursor()
            cursor.execute("SELECT 1")
            cursor.fetchone()
            return jsonify({"status": "✅ Database Connection Successful!"}), 200
        except Error as e:
            logger.error(f"Error: {str(e)}")
            return jsonify({"status": "❌ Query Failed", "error": str(e)}), 500
        finally:
            cursor.close()
            db.close()
    else:
        return jsonify({"status": "❌ Database Connection Failed"}), 500

# ---------------- HEALTH END ------------------------------------------------------------

@app.route("/login", methods=["POST"])
# @limiter.limit(
#     "5 per minute",
#     key_func=lambda: (
#         (request.get_json(silent=True) or {}).get("credential", "").lower()
#         or get_remote_address()
#     )
# )
@limiter.limit("5 per minute")
def login():
    logger.info("login")
    db = None
    cur = None

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "All data required"}), 400

    credential = data.get("credential", "").strip()
    password = data.get("password", "").strip()

    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute(
            "SELECT id, full_name, email, phone, password, role, status "
            "FROM users WHERE email=%s OR phone=%s",
            (credential, credential)
        )
        user = cur.fetchone()
        if not user:
            return jsonify({"message": "User not found"}), 401

        if not check_password_hash(user["password"], password):
            return jsonify({"message": "Invalid credentials"}), 401

        if user["status"] != "verified":
            return jsonify({
                "error": "Account not active"
            }), 403

#----- check tables ---------------------------
        # if user["role"] == "company":
        #     cur.execute("SELECT * FROM company_info WHERE company_id=%s",(user["id"],))
        #     comp = cur.fetchone()
        #     if not comp:
        #         logo_url = "https://img.icons8.com/?size=100&id=53426&format=png"
        #         cur.execute("INSERT INTO company_info(company_id, name, email, contact_no, logo) VALUES (%s, %s, %s, %s, %s)",
        #                     (user["id"], user["full_name"], user["email"], user["phone"], logo_url))
        #         db.commit()

        if user["role"] == "seeker":
            cur.execute("SELECT * FROM seeker_personal_info WHERE seeker_id=%s",(user["id"],))
            seek = cur.fetchone()
            if not seek:
                p_url = "https://img.freepik.com/free-icon/user_318-388892.jpg"
                cur.execute(
                    "INSERT INTO seeker_personal_info (seeker_id, name, photo) VALUES (%s, %s, %s)",
                    (user["id"],user["full_name"], p_url)
                )

                cur.execute(
                    "INSERT INTO seeker_professional_info (seeker_id) VALUES (%s)",
                    (user["id"],)
                )

                db.commit()
# ----- check table end --------------------------------------

        token = generate_token(
            user_id=user["id"],
            role=user["role"],
            status=user["status"]
        )

        print(f"\n\nTOKEN CREATED SUCESSFULLY\n\n")

        # send alert in email
        try:
            response = email_templates.templates.login_alert(current_time_date(),user["full_name"].split()[0])
            send_mail(response["subject"], response["body"], user["email"], "html")
            
            
        except Exception as e:
            logger.error(f"Email send error: {str(e)}")
            print("Email failed:", e)

        return jsonify({
            "token": token,
            "role": user["role"],
            "status": user["status"]
        }), 200

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        print("LOGIN ERROR:", e)
        return jsonify({"error": "Internal server error"}), 500

    finally:
        cur.close()
        db.close()

@app.route("/signup", methods=["POST"])
def sign_up():
    logger.info("Signup")
    data = request.get_json(silent=True)
    print(data)

    if not data:
        return jsonify({"message": "All data requred"}), 400
    
    required_fields = ["name", "email", "phone", "password", "role"]
    missing = [f for f in required_fields if f not in data or not data[f]]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400
    
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    phone = data.get("phone", "").strip()
    password = data.get("password", "").strip()
    role = data.get("role", "").strip()
    hashed_password = generate_password_hash(password)

    #check email and phone in db
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("SELECT * FROM users WHERE email=%s",(email,))
        res = cur.fetchone()
        if res:
            return jsonify({"message": "The email is already exist"})
        
        cur.execute("SELECT * FROM users WHERE phone=%s",(phone,))
        re = cur.fetchone()
        if re:
            return jsonify({"message": "The phone number is already exist"})
        
    except Exception:
        logger.error(f"Error: {str(e)}")
        return jsonify({"message": "Internal server error or busy now"})
    finally:
        if db and db.is_connected():
            cur.close()
            db.close()

    # CHECK PROFILE URL code
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        while True:
            code = generate_url_code()
            cur.execute("SELECT * FROM users WHERE url_code=%s",(code,))
            r = cur.fetchone()
            if not r:
                url_code = code
                break
            else:
                continue
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"error": f"{str(e)}"})
    finally:
        cur.close()
        db.close()
            

    verify_email = validate_email_adress(email)
    if not verify_email["status"]:
        return jsonify({"message": "Invalid email adress"}), 400
    
    phone_check = verify_phone_number(phone)
    if not phone_check["status"]:
        return jsonify({"message": "Invalid mobile number"}), 400

    #create uuid and send varification link
    token = str(uuid.uuid4())
    url = f"https://dt20tzx0-5000.inc1.devtunnels.ms/api/verify-email/{token}"

    response = email_templates.templates.verify_email_templetes(url, email)
    send_mail(response["subject"],response["body"], email, "html")


    
    
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        
        cur.execute(
            "INSERT INTO users(full_name, email, phone, password, role, status, visibility, verification_token, url_code, created_at) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (name, email, phone, hashed_password, role, "unverified","public", token, url_code, current_time_date())
        )
        db.commit()

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"message": "Internal server error"}), 500

    finally:
        if db and db.is_connected():
            cur.close()
            db.close()

    return jsonify({
        "message": "Signup successful. Please verify your email."
    }), 201



@app.route("/logout", methods=["POST"])
@token_required
def logout():
    logger.info("logout")
    db = get_db_connection()
    cur = db.cursor()

    try:
        cur.execute(
            "INSERT INTO revoked_tokens (jti) VALUES (%s)",
            (request.jti,)
        )
        db.commit()
        
        return jsonify({"message": "Successfully logged out. Token revoked."}), 200

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"error": "Logout failed", "details": str(e)}), 500

    finally:
        cur.close()
        db.close()




#-------------------------- END POINT SECTION END ---------------------------------------------



# pdf_bytes = base64.b64decode(pdf_base64) add in db

# pdf_base64 = base64.b64encode( send to frontend
#     row["incorporation_certificate"]
# ).decode("utf-8")


if __name__ == "__main__":

    # app.run(debug=True)
    # app.run(host="127.0.0.1", port=5000, debug=True)


    logger.info("Server starting on http://127.0.0.1:5000")
    print("Server starting on http://127.0.0.1:5000")
    serve(app, host="127.0.0.1", port=5000)

    # python -m watchdog.watchmedo auto-restart --patterns="*.py" --recursive -- python app.py   
    # run commant for devlopement
