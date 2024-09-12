from flask import jsonify, request
from app.modules.main.service.User_Service import UserService

# 

class User_Controller:

    def create_user():
        data = request.get_json()
        user = UserService.create_user(data)
        return jsonify({"message": "User created successfully!", "user": user.id}), 201

    def get_all_users(self):
        try:
            users = UserService.get_all_users()
            if users is None:
                return jsonify({"message": "No users found"}), 204

            users_list = [
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "mobile": user.mobile,
                    "dob": user.dob
                }
                for user in users
            ]
            
            return jsonify(users_list), 200
        
        except Exception as e:
            # Log the exception details if needed
            print(f"An error occurred: {str(e)}")
            return jsonify({"message": "An error occurred while retrieving users"}), 500

    def get_user_by_id(self ,user_id):
        user = UserService.get_user_by_id(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 204
        user_data = {"id": user.id, "name": user.name, "email": user.email, "mobile": user.mobile, "role": user.role, "dob": user.dob}
        return jsonify(user_data), 200

    def update_user(self,user_id):
        data = request.get_json()
        user = UserService.update_user(user_id, data)
        if not user:
            return jsonify({"message": "User not found"}), 204
        return jsonify({"message": "User updated successfully!"}), 200

    def delete_user(self,user_id):
        success = UserService.delete_user(user_id)
        if not success:
            return jsonify({"message": "User not found"}), 204
        return jsonify({"message": "User deleted successfully!"}), 200
