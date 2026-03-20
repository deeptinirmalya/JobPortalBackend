from security.jwt_utils import token_required, role_required
from flask import Blueprint, request, jsonify
from database.database import get_db_connection
from logger_config.loger_config import get_logger
import requests
from dotenv import load_dotenv
import os

interview_bp = Blueprint('interview', __name__)

load_dotenv()
logger = get_logger()



@interview_bp.route('/interview', methods=['POST'])
@token_required
@role_required("seeker")
def interview_practice():
    logger.info("Interview Practice End Point Hit")

    access_key = os.getenv("ACCESS_KEY")
    # print("access key: ",access_key)

    user_id = request.user_id
    # user_id = 123

    
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message required"}), 400

    try:
        # db = get_db_connection()
        # cur = db.cursor(dictionary=True)

        url = f"http://localhost:5002/interview/{user_id}"

        headers = {
            "X-Acces-Key": access_key,
            "Content-Type": "application/json"
        }

        data = {
            "message": data["message"]
        }

        response = requests.post(url, json=data, headers=headers)

        # print("\n\nResponse from interview end point:",response.json())


        return jsonify({
            "user_id": user_id,
            "response": response.json()["response"]
        })

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"err": str(e)})
    # finally:
    #     cur.close()
    #     db.close()


