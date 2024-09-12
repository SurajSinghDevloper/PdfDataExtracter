from flask import Blueprint,request
from app.modules.main.controllers.OperationalDataContoller import OperationalDataController
from app.modules.main.controllers.auth_middleware import token_required

operational_data_bp = Blueprint('operational_data_bp', __name__)

@operational_data_bp.route('/operational-data/uploaded-by/<int:uploaded_by>', methods=['GET'])
@token_required
def get_data_by_uploaded_by(uploaded_by):
    operationalDataContoller = OperationalDataController()
    return operationalDataContoller.get_data_by_uploaded_by(uploaded_by)

@operational_data_bp.route('/operational-data/is-printed/<int:is_printed>', methods=['GET'])  # uri => /operational-data/is-printed/1?page=2&limit=12
@token_required
def get_data_by_is_printed(is_printed):
    operationalDataContoller = OperationalDataController()
    return operationalDataContoller.get_data_by_is_printed(is_printed)

@operational_data_bp.route('/operational-data/created-at-range', methods=['GET'])
@token_required
def get_data_by_created_at_range():
    operationalDataContoller = OperationalDataController()
    return operationalDataContoller.get_data_by_created_at_range()


@operational_data_bp.route('/operational-data/mark', methods=['POST'])
@token_required
def mark_printStatus():
    operationalDataContoller = OperationalDataController()
    return operationalDataContoller.mark_data_printed()

@operational_data_bp.route('/operational-data/ac-no', methods=['GET'])
@token_required
def distinct_ac():
    operationalDataContoller = OperationalDataController()
    return operationalDataContoller.get_distinct_acNo()

@operational_data_bp.route('/operational-data/all-data', methods=['GET'])
@token_required
def get_all_operational_data():
    operationalDataContoller = OperationalDataController()
    return operationalDataContoller.get_data_by_Sl_Ac()
