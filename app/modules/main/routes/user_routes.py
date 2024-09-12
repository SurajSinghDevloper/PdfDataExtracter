from flask import Blueprint
from app.modules.main.controllers.User_Controller import User_Controller
from app.modules.main.controllers.auth_middleware import token_required

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/new-users', methods=['POST'])
@token_required
def create_user():
    user_controller = User_Controller()
    return user_controller.create_user()

@user_bp.route('/all-users', methods=['GET'])
@token_required
def get_allUsers():
    user_controller = User_Controller()
    return user_controller.get_all_users()

@user_bp.route('/users/<int:user_id>', methods=['GET'])
@token_required
def get_user(user_id):
    user_controller = User_Controller()
    return user_controller.get_user_by_id(user_id)

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@token_required
def update_user(user_id):
    user_controller = User_Controller()
    return user_controller.update_user(user_id)

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@token_required
def delete_user(user_id):
    user_controller = User_Controller()
    return user_controller.delete_user(user_id)
