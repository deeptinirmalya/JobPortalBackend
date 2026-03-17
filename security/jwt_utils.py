import jwt
import uuid
from functools import wraps
from flask import request, jsonify
from datetime import datetime, timedelta, timezone
from database.database import get_db_connection
import os

JWT_SECRET = os.getenv("JWT_SECRET_KEY")
JWT_ALGO = "HS256"
JWT_EXP_HOURS = 2


def generate_token(user_id, role, status):
    now = datetime.now(timezone.utc)

    payload = {
        # ----
        "jti": str(uuid.uuid4()), # Generate a unique ID for this token
        # --
        "user_id": user_id,
        "role": role,
        "status": status,
        "iat": now,
        "exp": now + timedelta(hours=JWT_EXP_HOURS)
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)
    return token


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization")
        # print(f"DEBUG: Received Authorization Header: {auth}")

        if not auth or not auth.startswith("Bearer "):
            return jsonify({"error": "Authorization token missing"}), 401

        token = auth.split(" ")[1]

        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
            
            # --- BLACKLIST CHECK START ---
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
            db = get_db_connection()
            cur = db.cursor()
            cur.execute("SELECT id FROM revoked_tokens WHERE jti = %s", (payload['jti'],))
            revoked = cur.fetchone()
            cur.close()
            db.close()

            if revoked:
                return jsonify({"error": "Token has been revoked (logged out)"}), 401
            # --- BLACKLIST CHECK END ---

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        request.user_id = payload["user_id"]
        request.role = payload["role"]
        request.status = payload["status"]
        request.jti = payload["jti"]

        return f(*args, **kwargs)
    return wrapper


def role_required(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if request.role not in allowed_roles:
                return jsonify({"error": "Forbidden"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator
