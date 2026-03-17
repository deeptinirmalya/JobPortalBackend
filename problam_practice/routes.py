from utils.utils import current_date, current_time_date
from database.database import get_db_connection
from flask import Blueprint, jsonify, request
from security.jwt_utils import token_required, role_required
import random
import requests

problam_bp = Blueprint('problem', __name__)



@problam_bp.route('/get_problem', methods=['POST'])
@token_required
@role_required("seeker")
def get_question():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"message": "All data required"}), 400
    level = data.get("level", "").strip()

    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("SELECT MAX(id) AS max_id FROM problames")
        row = cur.fetchone()

        if not row or not row["max_id"]:
            return jsonify({"message": "No problems available"}), 404

        max_id = row["max_id"]

        for _ in range(10):  # prevent infinite loop
            rand_id = random.randint(1, max_id)
            cur.execute(
                "SELECT id, title, description FROM problames WHERE id = %s AND level=%s",
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
        return jsonify({"error": str(e)}), 500

    finally:
        cur.close()
        db.close()



@problam_bp.route('/check_problem', methods=['POST'])
@token_required
@role_required("seeker")
def check_problame():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"message": "All data required"}), 400
    
    problam_id = data.get("problam_id", "").strip()
    language = data.get("language", "").strip()
    user_code = data.get("user_code", "").strip()
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT test_input, expected_output FROM problames WHERE id=%s",(problam_id))
        problame_details = cur.fetchone()

        url = "https://emkc.org/api/v2/piston/execute"
        payload = {
            "language": language,
            "version": "*",
            "files": [{"content": user_code}],
            "stdin": problame_details["test_input"]
        }
        
        response = requests.post(url, json=payload)
        result = response.json()
        
        # 3. Validation Logic
        actual_output = result.get('run', {}).get('stdout', '').strip()
        error_output = result.get('run', {}).get('stderr', '').strip()

        if error_output:
            return jsonify({"message": f"❌ Incorrect (Runtime Error): {error_output}"})
        
        if actual_output == problame_details["expected_output"]:
            return jsonify({"message": f"✅ Correct! Your code passed the test case."})
        else:
            return jsonify({"message": f"❌ Incorrect"})
    except Exception as e:
        print(str(e))
        return jsonify({"error":f"{str(e)}"})
    finally:
        cur.close()
        db.close()


