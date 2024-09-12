from flask import Blueprint
from app.modules.main.controllers.Auth_Controller import Auth_Controller

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/authenticate', methods=['POST'])
def login():
    return Auth_Controller.login()

@auth_bp.route('/register', methods=['POST'])
def register():
    return Auth_Controller.signup()
