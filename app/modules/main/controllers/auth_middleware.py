from functools import wraps
import jwt
from flask import request, abort
from flask import current_app
from app.modules.main.models.User_Model import User_Model
from app.modules.main.service.User_Service import UserService

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None
#         if "Authorization" in request.headers:
#             token = request.headers["Authorization"].split(" ")[1]
#         if not token:
#             return {
#                 "message": "Authentication Token is missing!",
#                 "data": None,
#                 "error": "Unauthorized"
#             }, 401
#         try:
#             data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
#             print("TOKEN_DATA ===============> ",data)
#             current_user = UserService.get_user_by_email(data["user_email"])
#             if current_user is None:
#                 return {
#                     "message": "Invalid Authentication token!",
#                     "data": None,
#                     "error": "Unauthorized"
#                 }, 401
#             if not current_user.active:
#                 abort(403)
#         except jwt.ExpiredSignatureError:
#             return {
#                 "message": "Token has expired!",
#                 "data": None,
#                 "error": "Unauthorized"
#             }, 401
#         except jwt.InvalidTokenError:
#             return {
#                 "message": "Invalid token!",
#                 "data": None,
#                 "error": "Unauthorized"
#             }, 401
#         except Exception as e:
#             return {
#                 "message": "Something went wrong",
#                 "data": None,
#                 "error": str(e)
#             }, 500

#         return f(current_user, *args, **kwargs)

#     return decorated
    
    
    
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = UserService.get_user_by_email(data["user_email"])
            if current_user is None:
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
            if not current_user.active:
                abort(403)
        except jwt.ExpiredSignatureError:
            return {
                "message": "Token has expired!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        except jwt.InvalidTokenError:
            return {
                "message": "Invalid token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        # Determine if the decorated function accepts `current_user`
        if 'current_user' in f.__code__.co_varnames:
            return f(current_user, *args, **kwargs)
        else:
            return f(*args, **kwargs)

    return decorated
