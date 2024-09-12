from flask import request, current_app,jsonify
import jwt
from app.modules.main.service.User_Service import UserService
from datetime import datetime, timedelta

class Auth_Controller:

    @staticmethod
    def login():
        try:
            data = request.json
            if not data:
                return {
                    "message": "Please provide user details",
                    "data": None,
                    "error": "Bad request"
                }, 400

            # Fetch the user by email
            user = UserService.get_user_by_email(data.get('email'))
            if user and UserService.verify_password(user.password, data.get('password')):
                try:
                    # Generate token with a 24-hour expiration
                    token = jwt.encode(
                        {"user_email": user.email, "exp": datetime.utcnow() + timedelta(hours=24)},
                        current_app.config["SECRET_KEY"],
                        algorithm="HS256"
                    )
                    user_roles = UserService.role_by_userid(user.id)
                    foundUser = {
                        "id": user.id,
                        "name": user.name,
                        "email": user.email,
                        "mobile":user.mobile,
                        "dob":user.dob,
                        "role":user_roles
                    }
                    return {
                        "message": "Successfully Authenticated",
                        "data": {"token": token, "user": foundUser}
                    }, 200
                except Exception as e:
                    return {
                        "message": "Something went wrong",
                        "error": str(e),
                        "data": None
                    }, 500
            else:
                return {
                    "message": "Invalid email or password",
                    "data": None,
                    "error": "Unauthorized"
                }, 401

        except Exception as e:
            return {
                "message": "Something went wrong!",
                "error": str(e),
                "data": None
            }, 500

    def signup():
        data = request.get_json()
        user = UserService.create_user(data)
        return jsonify({"message": "User created successfully!", "user": user.id}), 201