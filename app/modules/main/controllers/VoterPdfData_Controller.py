from flask import Blueprint, jsonify, request
from app.modules.main.service.VoterPdfData_Service import VoterPdfData_Service

class VoterPdfData_Controller:
    def create_voter_data(self):
        pdf_files = request.files.getlist('pdf_files')
        uploader_id = request.form.get('uploader_id')
        lot_no=request.form.get('lot_no')
        lot_no=0
        if not pdf_files or not isinstance(pdf_files, list):
            return jsonify({'error': 'A list of PDF files is required'}), 400
        # uploader_id=1
        voter_pdf_service = VoterPdfData_Service() 
        results = []
        for pdf_file in pdf_files:
            # print("files are =======>   ",pdf_file.filename)  
            result = voter_pdf_service.process_pdf_list(pdf_file,uploader_id,lot_no)
            results.append(result)

        return jsonify({'message': 'Processing completed', 'results': results}), 200
