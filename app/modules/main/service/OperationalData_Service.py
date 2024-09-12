from app.db.db import db
from sqlalchemy.exc import SQLAlchemyError
from app.modules.main.models.OperationalData import OperationalData
from app.modules.main.repo.OperationalDataRepository import OperationalDataRepository
class OperationalData_Service:
    
    @staticmethod
    def create_operational_data(pdfData):
        try:
            # print("FROM OPERATIONAL DATA ======",pdfData)
            operational_data = OperationalData(
                date=pdfData.created_at, 
                id=pdfData.id, 
                barcode_no=pdfData.barcode_no,
                id_no=pdfData.id_no,
                form_ref_no=pdfData.form_ref_no,
                sub_id=pdfData.sub_id,
                name=pdfData.name,
                father_name=pdfData.father_name,
                monther_name=pdfData.monther_name,
                husband_name=pdfData.husband_name,
                wife_name=pdfData.wife_name,
                other_gurdian=pdfData.other_gurdian,
                address=pdfData.address,
                district=pdfData.district,
                mobile_no=pdfData.mobile_no,
                state_code=pdfData.state_code,
                ac_no=pdfData.ac_no,
                part_no=pdfData.part_no,
                sl_no=pdfData.sl_no,
                filename=pdfData.filename,
                uploadedBy=pdfData.uploadedBy,
                created_at=pdfData.created_at,
                lot_no=pdfData.lot_no,
                isPrinted=False,
                printedBy=0,
                printCount=0,
                # page_no=0,
                # sticker_no=0,
            )
            db.session.add(operational_data)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def get_operational_data_by_uploaded_by(uploaded_by):
        return OperationalDataRepository.get_by_uploaded_by(uploaded_by)

    @staticmethod
    def get_operational_data_by_is_printed(is_printed, page, limit):
        return OperationalDataRepository.get_by_is_printed(is_printed, page, limit)

    @staticmethod
    def get_operational_data_by_created_at_range(start_date, end_date):
        return OperationalDataRepository.get_by_created_at_range(start_date, end_date)
    
    @staticmethod
    def get_data_by_id_and_mark_print(ids):
        try:
            for id in ids:
                # Retrieve the record by id
                opdData = OperationalDataRepository.getDataById(id)
                
                # Check if data exists
                if opdData:
                    # Mark the data as printed
                    opdData.isPrinted = True
                    
                    # Add the updated record to the session
                    db.session.add(opdData)
            
            # Commit the session after all updates
            db.session.commit()

        except Exception as e:
            # Rollback in case of error
            db.session.rollback()
            raise e
    
    @staticmethod
    def get_distinct_ac():
        return OperationalDataRepository.getDistinctAcNo()
    
    @staticmethod
    def get_count_of_details(type):
        found_data=OperationalDataRepository.getLatestRecord()
        pageNum=0
        stickerNum=0
        lotNum=0
        if type=='pageNo':
            pageNum=found_data.page_no
            return pageNum
        if type=='stickerNo':
            stickerNum=found_data.sticker_no
            return stickerNum
        if type=='lotNo':
            lotNum=found_data.lot_no
            return lotNum

    @staticmethod
    def get_all_data_by_ac_and_sl_no():
        return OperationalDataRepository.get_all_voter_data_by_ac_no_sl_no()