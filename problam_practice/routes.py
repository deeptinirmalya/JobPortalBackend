from utils.utils import current_date, current_time_date
from database.database import get_db_connection
from flask import Blueprint, jsonify, request
from security.jwt_utils import token_required, role_required
from logger_config.loger_config import get_logger
import random
import requests

problam_bp = Blueprint('problem', __name__)

logger = get_logger()

@problam_bp.route('/get_problem/<string:level>', methods=['GET'])
# @token_required
# @role_required("seeker")
def get_question(level):
    logger.info("get get_question fro practice")

    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("SELECT MAX(id) AS max_id FROM problames")
        row = cur.fetchone()

        if not row or not row["max_id"]:
            return jsonify({"message": "No problems available"}), 404

        max_id = row["max_id"]

        for _ in range(10): 
            rand_id = random.randint(1, max_id)
            cur.execute(
                "SELECT id, title, description FROM problames WHERE id = %s AND leven=%s",
                (rand_id, level)
            )
            problem = cur.fetchone()
            if problem:
                return jsonify({
                    "success": True,
                    "problem_id": problem["id"],
                    "title": problem["title"],
                    "description": problem["description"]
                })

        return jsonify({"message": "Could not fetch problem"}), 500

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

    finally:
        cur.close()
        db.close()



# @problam_bp.route('/check_problem', methods=['POST'])
# # @token_required
# # @role_required("seeker")
# def check_problame():
#     data = request.get_json(silent=True)
#     if not data:
#         return jsonify({"message": "All data required"}), 400
    
#     problam_id = data.get("problam_id", "").strip()
#     language = data.get("language", "").strip()
#     user_code = data.get("user_code", "").strip()
#     try:
#         db = get_db_connection()
#         cur = db.cursor(dictionary=True)
#         cur.execute("SELECT test_input, expected_output FROM problames WHERE id=%s",(problam_id,))
#         problame_details = cur.fetchone()

#         url = "https://emkc.org/api/v2/piston/execute"
#         payload = {
#             "language": language,
#             "version": "*",
#             "files": [{"content": user_code}],
#             "stdin": problame_details["test_input"]
#         }
        
#         response = requests.post(url, json=payload)
#         result = response.json()
        
#         # 3. Validation Logic
#         actual_output = result.get('run', {}).get('stdout', '').strip()
#         error_output = result.get('run', {}).get('stderr', '').strip()

#         if error_output:
#             return jsonify({"message": f"❌ Incorrect (Runtime Error): {error_output}"})
        
#         if actual_output == problame_details["expected_output"]:
#             return jsonify({"message": f"✅ Correct! Your code passed the test case."})
#         else:
#             return jsonify({"message": f"❌ Incorrect"})
#     except Exception as e:
#         print(str(e))
#         return jsonify({"error":f"{str(e)}"})
#     finally:
#         cur.close()
#         db.close()




JDOODLE_CLIENT_ID = "cf5aef5f0f796e599fc67b4ea19aca38"
JDOODLE_CLIENT_SECRET = "2f922f48314c1a1a28092a4b212cde8ecbb8e084193c2c005d003f2688ebf582"

# Language Mapping for JDoodle
# language: JDoodle language code
# versionIndex: 0 usually refers to the latest/default version
SUPPORTED_LANGUAGES = {
    "python": {"lang": "python3", "versionIndex": "4"}, # Python 3.10+
    "java": {"lang": "java", "versionIndex": "4"},     # JDK 17
    "c": {"lang": "c", "versionIndex": "5"},           # GCC 11.1.0
    "cpp": {"lang": "cpp17", "versionIndex": "1"}      # G++ 17
}

@problam_bp.route('/check_problem', methods=['POST'])
def check_problame():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"message": "All data required"}), 400

    problam_id = data.get("problam_id")
    language = data.get("language", "").strip().lower()
    user_code = data.get("user_code", "").strip()

    if language not in SUPPORTED_LANGUAGES:
        return jsonify({"message": "Unsupported language"}), 400

    db = None
    cur = None

    try:
        # 1. Fetch Problem from DB
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT test_input, expected_output FROM problames WHERE id=%s", (problam_id,))
        problame = cur.fetchone()

        if not problame:
            return jsonify({"message": "Problem not found"}), 404

        # 2. Prepare JDoodle Payload
        lang_config = SUPPORTED_LANGUAGES[language]
        url = "https://api.jdoodle.com/v1/execute"

        payload = {
            "clientId": JDOODLE_CLIENT_ID,
            "clientSecret": JDOODLE_CLIENT_SECRET,
            "script": user_code,
            "stdin": str(problame["test_input"]),
            "language": lang_config["lang"],
            "versionIndex": lang_config["versionIndex"]
        }

        # 3. Request Execution
        response = requests.post(url, json=payload, timeout=10)
        result = response.json()

        # JDoodle returns 'output' for both stdout and stderr combined usually, 
        # but also provides a 'statusCode'
        stdout = result.get("output", "").strip()
        
        # 4. Compare results
        expected_output = str(problame["expected_output"]).strip()

        if stdout == expected_output:
            return jsonify({"status": "success", "message": "Correct"})
        else:
            return jsonify({
                "status": "fail",
                "message": "Incorrect",
                "expected": expected_output,
                "got": stdout,
                "cpuTime": result.get("cpuTime"),
                "memory": result.get("memory")
            })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cur: cur.close()
        if db: db.close()