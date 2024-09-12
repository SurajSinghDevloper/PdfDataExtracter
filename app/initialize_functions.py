from flask import Flask
from flasgger import Swagger
from app.db.db import db
from app.modules.main.routes.user_routes import user_bp
from app.modules.main.routes.auth_routes import auth_bp
from app.modules.main.routes.voter_pdf_data_routes import voterPdfData_bp
from app.modules.main.routes.operational_data_route import operational_data_bp
from flask_cors import CORS

def initialize_route(app: Flask):
    # Apply CORS to the entire app
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    with app.app_context():
        # Registering the user blueprint
        app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
        # Registering the user blueprint
        app.register_blueprint(user_bp, url_prefix='/api/v1/user')
        # Registering the Voter pdf data blueprint
        app.register_blueprint(voterPdfData_bp, url_prefix='/api/v1/voter-pdf-data')
        # Registering the Operational data blueprint
        app.register_blueprint(operational_data_bp, url_prefix='/api/v1/operational')

def initialize_db(app: Flask):
    with app.app_context():
        db.init_app(app)
        db.create_all()

def initialize_swagger(app: Flask):
    with app.app_context():
        swagger = Swagger(app)
        return swagger
