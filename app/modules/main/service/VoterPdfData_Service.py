import pdfplumber
import pytesseract
import cv2
import re
from pyzbar.pyzbar import decode
import numpy as np
from PIL import Image
from app.db.db import db
from sqlalchemy.exc import SQLAlchemyError
from app.modules.main.models.VoterPDFData import VoterPdfData_Model 
from app.modules.main.service.OperationalData_Service import OperationalData_Service

class VoterPdfData_Service:

    @staticmethod
    def preprocess_image(image):
        gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
        _, thresh_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return Image.fromarray(thresh_image)

    @staticmethod
    def extract_barcode_and_text(image):
        barcodes = decode(np.array(image))
        barcode_data = [barcode.data.decode('utf-8') for barcode in barcodes]
        text_data = pytesseract.image_to_string(image)
        return barcode_data, text_data

    @staticmethod
    def extract_address(text):
     lines = text.split('\n')
     address_lines = []
     collecting_address = False
    
     for line in lines:
        if line.startswith("Address"):
            collecting_address = True
            address_lines.append(line.split("Address")[-1].strip())
        elif line.startswith("Mobile No"):
            collecting_address = False
            break
        elif collecting_address:
            address_lines.append(line.strip())
    
    # Join all collected address lines
     complete_address = ' '.join(address_lines).strip()
     return complete_address



    @staticmethod
    def parse_text(text):
        lines = text.split('\n')
        parsed_data = {
            'BarcodeNo': None,
            'IdNo': None,
            'FormRefNo': None,
            'SubId': None,
            'Name': None,
            'FatherName': None,
            'MotherName':None,
            'Husband':None,
            'WifeName':None,
            'OtherGurdian':None,
            'Address': None,
            'MobileNo': None,
            'Filename': None,
            'StateCode': None,
            'AcNo': None,
            'District':None,
            'PartNo': None,
            'SlNo': None,
            'uploadedBy':None,
            'LotNo':None
        }
        count =0
        for line in lines:
            count=count+1
            # print("LINE ========= OF PDF =====>",line,count)
            if count ==1:
                parsed_data['BarcodeNo'] = line.strip()
            elif count ==2:
                parsed_data['IdNo'] = line.strip()
            elif "Form Ref No." in line:
                parts = line.split()
                if len(parts) > 3:
                    parsed_data['FormRefNo'] = parts[3]
                if len(parts) > 4:
                    parsed_data['SubId'] = parts[4]
            elif line.startswith("Name"):
                parsed_data['Name'] = line.split("Name")[-1].strip()
            elif line.startswith("Father's Name")or line.startswith("Husband")or line.startswith("Other")or line.startswith("Mother's Name")or line.startswith("Wife's Name"):
                if line.startswith("Father's Name"):
                    parsed_data['FatherName'] = line.split("Father's Name")[-1].strip()
                if line.startswith("Husband"):
                    parsed_data['Husband'] = line.split("Husband's Name")[-1].strip()
                if line.startswith("Other"):
                    parsed_data['OtherGurdian'] = line.split("Other")[-1].strip()
                if line.startswith("Mother"):
                    parsed_data['MotherName'] = line.split("Mother's Name")[-1].strip()
                if line.startswith("Wife's Name"):
                    parsed_data['WifeName'] = line.split("Wife's Name")[-1].strip()
            elif line.startswith("Address"):
                # parsed_data['Address'] = line.split("Address")[-1].strip()
                parsed_data['Address'] = VoterPdfData_Service.extract_address(text)
                temp_add = line.split("Address")[-1].strip()
                # Use regex to extract a 6-digit pin code from the end of the address line
                pin_code_match = re.search(r'\b\d{6}\b', temp_add)
                if pin_code_match:
                   parsed_data['District'] = pin_code_match.group()
            elif line.startswith("Mobile No"):
                parsed_data['MobileNo'] = line.split("Mobile No")[-1].strip()
        return parsed_data

    @staticmethod
    def extract_filename_components(filename):
        components = filename.split('_')
        # print("COMPONENT ARE =====================> ",components)
        statecode = components[0][1:]
        acNo = components[1]
        partNo = components[2]
        slNo = components[3]
        # print("STATE CODE => ",statecode," AC NO => ",acNo,"  PART NO => ",partNo," SL NO => ",slNo)

        return statecode, acNo, partNo, slNo
    

    def process_pdf_list(self, pdf_file,uploader_id,lot_no):
        filename = pdf_file.filename
        # print("NAME OF FILE ========> ",filename)
        data = []
        statecode, acNo, partNo, slNo = self.extract_filename_components(filename)

        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                for img in page.images:
                    if 'bbox' in img:
                        bbox = img['bbox']
                        pil_image = page.to_image().original.crop(bbox)
                        preprocessed_image = self.preprocess_image(pil_image)
                        barcodes, image_text = self.extract_barcode_and_text(preprocessed_image)
                        parsed_data = self.parse_text(image_text)
                        parsed_data.update({
                            'Filename': filename,
                            'StateCode': statecode,
                            'AcNo': acNo,
                            'PartNo': partNo,
                            'SlNo': slNo,
                            'BarcodeNo': barcodes[0] if barcodes else ""
                        })
                        data.append(parsed_data)
                parsed_data = self.parse_text(page_text)
                parsed_data.update({
                    'Filename': filename,
                    'StateCode': statecode,
                    'AcNo': acNo,
                    'PartNo': partNo,
                    'SlNo': slNo
                })
                parsed_data.update({
                    'uploadedBy': uploader_id,
                    'LotNo': lot_no
                })
                data.append(parsed_data)
        self.save_data(data)  
        return f"Processed successfully: {filename}"

    @staticmethod
    def save_data(data):
        try:
            for record in data:
                # print("THE MOBILE NO OF CANDIDATE =========> ",record['MobileNo'])
                mobileNO = record['MobileNo']
                # print("Length MOBILE NO OF CANDIDATE =========> ",len(mobileNO))
                new_voter_pdf_data = VoterPdfData_Model(
                    barcode_no=record['BarcodeNo'],
                    id_no=record['IdNo'],
                    form_ref_no=record['FormRefNo'],
                    sub_id=record['SubId'],
                    name=record['Name'],
                    father_name=record['FatherName'],
                    monther_name=record['MotherName'],
                    husband_name=record['Husband'],
                    wife_name=record['WifeName'],
                    other_gurdian=record['OtherGurdian'],
                    address=record['Address'],
                    district=record['District'],
                    mobile_no = record['MobileNo'] if mobileNO and len(mobileNO) > 8 else "",
                    state_code=record['StateCode'],
                    ac_no=record['AcNo'],
                    part_no=record['PartNo'],
                    sl_no=record['SlNo'],
                    filename=record['Filename'],
                    lot_no=record['LotNo'],
                    uploadedBy=record['uploadedBy']
                )
                db.session.add(new_voter_pdf_data)
            db.session.commit()
            new_data = db.session.query(VoterPdfData_Model).order_by(VoterPdfData_Model.created_at.desc()).first()
            OperationalData_Service.create_operational_data(new_data)
            
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
    
    
    
    