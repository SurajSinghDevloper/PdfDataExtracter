from flask import Blueprint,request,jsonify
from app.modules.main.controllers.VoterPdfData_Controller import VoterPdfData_Controller
from app.modules.main.controllers.auth_middleware import token_required

voterPdfData_bp = Blueprint('voterPdfData', __name__)

@voterPdfData_bp.route('/process-pdf', methods=['POST'])
@token_required
def create_voter_data():
    voter_pdf_controller = VoterPdfData_Controller()
    return voter_pdf_controller.create_voter_data()
