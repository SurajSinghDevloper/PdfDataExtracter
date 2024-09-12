from flask import  jsonify, request
from app.modules.main.service.OperationalData_Service import OperationalData_Service

class OperationalDataController:
    def get_data_by_uploaded_by(self,uploaded_by):
        try:
            data = OperationalData_Service.get_operational_data_by_uploaded_by(uploaded_by)
            return jsonify([item.serialize() for item in data]) 
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    def get_data_by_is_printed(self,is_printed):
        try:
            page = request.args.get('page', default=1, type=int)
            limit = request.args.get('limit', default=12, type=int)
            data = OperationalData_Service.get_operational_data_by_is_printed(is_printed, page, limit)
            return jsonify([item.serialize() for item in data])
        except Exception as e:
            return jsonify({"error": str(e)}), 500

   
    def get_data_by_created_at_range(self):
        try:
            start_date = request.args.get('start_date')
            end_date = request.args.get('end_date')
            data = OperationalData_Service.get_operational_data_by_created_at_range(start_date, end_date)
            return jsonify([item.serialize() for item in data])
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def mark_data_printed(self):
        try:
            # Extract the list of ids from the request
            request_data = request.get_json()
            ids = request_data.get('ids', [])
            
            # If ids list is not empty, proceed
            if ids:
                data = OperationalData_Service.get_data_by_id_and_mark_print(ids)
                return jsonify({"message": "Data marked as printed successfully"}), 200
            else:
                return jsonify({"error": "No ids provided"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
           
            