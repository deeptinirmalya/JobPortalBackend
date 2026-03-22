from flask import Blueprint, jsonify, request
from database.database import get_db_connection
from utils.utils import current_time_date, upload_image, check_image_size
from security.jwt_utils import token_required, role_required
from logger_config.loger_config import get_logger



content_bp = Blueprint('content', __name__)

logger = get_logger()

@content_bp.route('/image_post', methods=['POST'])
@token_required
@role_required("seeker", "company")
def image_post():
    data = request.get_json(silent=True)
    print(data)

    required_fields = ["image", "caption"]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    image_base64 = data.get("image", "")
    caption = data.get("caption", "")
    status = data.get("status", "")

    if not image_base64:
        return jsonify({"message": "Image most required"}), 400

    if check_image_size(image_base64):
        image_url = upload_image(image_base64)
    else:
        return jsonify({"message": "Image is too large must be 3MB"}), 400
    
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("INSERT INTO photo_posts(user_id, photo_url, caption, status, created_at) VALUE(%s, %s, %s, %s, %s)",
                    (request.user_id, image_url, caption, status, current_time_date()))
        
        db.commit()
        return jsonify({"message": f"Upload sucessful with status{status}"})
    except Exception as e:
        db.rollback()
        print("error::==",str(e))
        return jsonify({"error": f"{str(e)}"})
    finally:
        db.close()
        cur.close()

    

@content_bp.route('/like_post', methods=['POST'])
@token_required
@role_required("seeker", "company")
def like_post():
    data = request.get_json(silent=True)

    print(f"row data like {data}")
    
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)
        cur.execute("SELECT * FROM photo_post_likes WHERE post_id=%s AND user_id=%s",(int(data.get("post_id")), request.user_id))
        res = cur.fetchone()
        if not res:
            cur.execute("INSERT INTO photo_post_likes(post_id, user_id, created_at) VALUE(%s, %s, %s)",
                        (int(data.get("post_id")), request.user_id, current_time_date()))
            
            cur.execute("UPDATE photo_posts SET like_count=like_count+1 WHERE id=%s",(int(data.get("post_id")),))
            db.commit()
            print("SUCESS FULLY LIKE")
            return jsonify({"message": f"Like sucessfull"})
        else:
            # print("already liked ")
            return jsonify({"message": f"ALREADY LIKED"})
    except Exception as e:
        db.rollback()
        return jsonify({"error": f"{str(e)}"})
    finally:
        db.close()
        cur.close()


@content_bp.route('/comment_post', methods=['POST'])
@token_required
@role_required("seeker", "company")
def comment_post():
    data = request.get_json(silent=True)
    print(f"row data coment {data}")
    # HARD validation
    if not data or not data.get("post_id") or not data.get("comment"):
        return jsonify({"error": "post_id and comment are required"}), 400

    try:
        post_id = int(data["post_id"])
        comment = data["comment"].strip()

        if not comment:
            return jsonify({"error": "Empty comment not allowed"}), 400

        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        # INSERT COMMENT
        cur.execute(
            """
            INSERT INTO photo_post_comments
            (post_id, user_id, comment_text, created_at)
            VALUES (%s, %s, %s, %s)
            """,
            (post_id, request.user_id, comment, current_time_date())
        )


        cur.execute(
            "UPDATE photo_posts SET comment_count = comment_count + 1 WHERE id = %s",
            (post_id,)
        )

        if cur.rowcount == 0:
            db.rollback()
            return jsonify({"error": "Invalid post_id"}), 400

        db.commit()
        print("SUCESS FULLY COMENT")
        return jsonify({"message": "Comment successful"})

    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cur.close()
        db.close()



@content_bp.route('/view_comments', methods=['POST'])
@token_required
@role_required("seeker", "company")
def view_comments():
    data = request.get_json(silent=True)
    print(data)

    # HARD validation
    if not data or not data.get("post_id"):
        return jsonify({"error": "post_id required"}), 400

    try:
        post_id = int(data["post_id"])

        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute(
            """
            SELECT
                c.comment_text,
                u.full_name,
            FROM photo_post_comments c
            JOIN users u ON u.id = c.user_id
            WHERE c.post_id = %s
            AND c.status = %s
            ORDER BY c.id DESC
            """,
            (post_id, "active")
        )

        comments = cur.fetchall()

        return jsonify({"comments": comments}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cur.close()
        db.close()


@content_bp.route('/view_posts', methods=['GET'])
@token_required
@role_required("seeker", "company")
def view_posts():
    try:
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))
        offset = (page - 1) * limit

        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute(
                    """
                    SELECT 
                        p.id, 
                        p.user_id, 
                        p.photo_url, 
                        p.caption, 
                        p.like_count, 
                        p.comment_count, 
                        u.full_name 
                    FROM photo_posts p
                    JOIN users u ON u.id = p.user_id
                    WHERE p.status = %s
                    ORDER BY p.id DESC
                    LIMIT %s OFFSET %s
                    """,
                    ("public", limit, offset)
                )

        posts = cur.fetchall()
        print(posts)
        return jsonify({
            "page": page,
            "limit": limit,
            "posts": posts
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cur.close()
        db.close()


@content_bp.route("/view_all_posts", methods=["GET"])
@token_required
@role_required("seeker", "company")
def view_all_posts():
    user_id = request.user_id
    logger.info(f"/view_all_posts of {user_id}")
    try:
        db = get_db_connection()
        cur = db.cursor(dictionary=True)

        cur.execute("SELECT * FROM photo_posts WHERE user_id=%s",(user_id,))
        res = cur.fetchall()

        return jsonify({"res": res})


    except Exception as e:
        logger.error(f"Error {str(e)}")
        return jsonify({"err": str(e)})
    finally:
        cur.close()
        db.close()