from email_validator import validate_email, EmailNotValidError
from dotenv import load_dotenv
from datetime import datetime
import cloudinary.uploader
import cloudinary
import base64
import requests
import json
import secrets
import string
import pytz
import os

load_dotenv()

IST = pytz.timezone("Asia/Kolkata")

def current_time_date():
    return datetime.now(IST).strftime("%d-%m-%Y %H:%M")

def current_date():
    return datetime.now(IST).strftime("%d-%m-%Y")

def current_time():
    return datetime.now(IST).strftime("%H:%M")



def send_mail(subject, body, reciver_email, body_tipe):
    url = "https://dt20tzx0-5001.inc1.devtunnels.ms/accept-email-iv"
    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": os.getenv("X-API-KEY")
    }

    payload = {
        "subject": subject,
        "body": body,
        "receiver_email": reciver_email,
        "body_type": body_tipe
    }

    response = requests.post(url, json=payload, headers=headers, timeout=10)
    return response



def check_image_size(image_base64: str) -> bool:
    MAX_SIZE = 3 * 1024 * 1024  # 3MB
    try:

        if ',' in image_base64:
            image_base64 = image_base64.split(',')[1]

        image_bytes = base64.b64decode(image_base64)
        return len(image_bytes) <= MAX_SIZE

    except (base64.binascii.Error, TypeError):
    
        return False

#======================================== FOR running server using "serve" ==============================================


def upload_image(image_base64: str) -> str:
    if not cloudinary.config().api_key:
        cloudinary.config(
            cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
            api_key=os.getenv("CLOUDINARY_API_KEY"),
            api_secret=os.getenv("CLOUDINARY_API_SECRET")
        )

    if not image_base64:
        raise ValueError("Image data missing")

    try:
        # Normalize base64 (handle both raw + full data URI)
        if not image_base64.startswith("data:image"):
            image_base64 = f"data:image/jpeg;base64,{image_base64}"

        result = cloudinary.uploader.upload(
            image_base64,
            folder="uploads",
            resource_type="image"
        )

        return result["secure_url"]

    except Exception as e:
        raise RuntimeError(f"Upload failed: {str(e)}")




def upload_resume(image_base64: str) -> str:
    if not cloudinary.config().api_key:
        cloudinary.config(
            cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
            api_key=os.getenv("CLOUDINARY_API_KEY"),
            api_secret=os.getenv("CLOUDINARY_API_SECRET")
        )

    if not image_base64:
        raise ValueError("Image data missing")

    # Normalize base64 format
    if not image_base64.startswith("data:image"):
        image_base64 = f"data:image/jpeg;base64,{image_base64}"

    try:
        result = cloudinary.uploader.upload(
            image_base64,
            folder="uploads",
            resource_type="image"
        )

        return result["secure_url"]

    except Exception as e:
        raise RuntimeError(f"Upload failed: {str(e)}")
    
#=======================================================================================


# def upload_image(image_base64: str) -> str:
#     if not image_base64:
#         raise ValueError("Image data missing")

#     try:

#         if not image_base64.startswith("data:image"):
#             image_base64 = f"data:image/jpeg;base64,{image_base64}"

#         result = cloudinary.uploader.upload(
#             image_base64,
#             folder="uploads",
#             resource_type="image"
#         )

#         return result["secure_url"]

#     except Exception as e:
#         raise RuntimeError(f"Upload failed: {str(e)}")


# def upload_resume(image_base64: str) -> str:

#     if ',' in image_base64:
#         image_base64 = image_base64.split(',')[1]

#     result = cloudinary.uploader.upload(
#         f"data:image/jpeg;base64,{image_base64}",
#         folder="uploads"
#     )

#     return result["secure_url"]


def generate_url_code():
    length = secrets.choice(range(12, 16))
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))



def verify_phone_number(phone_number):
    if not phone_number:
        return {"valid": False, "error": "Phone number is required", "status_code": 400}
    
    url = f'https://apilayer.net/api/validate?access_key={os.getenv("NUMBER_VERIFY")}&number={phone_number}&country_code=IN'
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return {"valid": False, "error": "API Connection Failed", "status_code": 500}
        
        result = response.json()
        
        if result.get('valid'):
            return {
                "status": True,
                "status_code": 200
            }
        else:
            return {"status": False,"status_code": 400}
            
    except Exception as e:
        return {"status": False, "error": str(e), "status_code": 500}
    

def validate_email_adress(email: str) -> dict:
    if not email:
        return {"status": False, "error": "Email is required"}

    try:
        validate_email(email)   # basic syntax + domain check
        return {"status": True}
    except EmailNotValidError as e:
        return {
            "status": False,
            "error": str(e)
        }
    


# Resume analyser:-========================

def analyze_resume_from_url(resume_url):
    
    OPENROUTER_API_KEY = os.getenv("MY_OPENROUTER_API_KEY")

    prompt = """
Analyze the resume image and extract structured information.

Return JSON only with:
name
email
phone
skills
education
experience
projects
summary
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": resume_url
                            }
                        }
                    ]
                }
            ]
        }
    )

    result = response.json()

    # print("API Response:")
    # print(json.dumps(result, indent=2))

    if "choices" not in result:
        raise Exception("API Error: " + json.dumps(result, indent=2))

    return result["choices"][0]["message"]["content"]