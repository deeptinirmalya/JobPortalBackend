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
def interview_practice():
    logger.info("Interview Practice End Point Hit")
    access_key = os.getenv("INTERVIEW_AI_ACCESS_KEY")
    user_id = 123 # Still hardcoded, but functional

    # print("access key: ", access_key)
    
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Message required"}), 400

    try:
        url = f"http://localhost:5002/interview/{user_id}"
        headers = {
            "X-Acces-Key": access_key, # Fixed Typo
            "Content-Type": "application/json"
        }

        # Forward the request
        response = requests.post(url, json={"message": data["message"]}, headers=headers)
        
        # Safely parse response
        resp_data = response.json()
        
        return jsonify({
            "user_id": user_id,
            "response": resp_data.get("response", "Sorry, the AI service is unavailable.")
        })

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"err": "Internal Server Error"}), 500
