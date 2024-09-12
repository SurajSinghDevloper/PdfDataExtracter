from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_
from app.modules.main.models.OperationalData import OperationalData 
from app.db.db import db 
from sqlalchemy import cast, Boolean,Integer

class OperationalDataRepository:

    @staticmethod
    def get_by_uploaded_by(uploaded_by):
        try:
            return OperationalData.query.filter_by(uploadedBy=uploaded_by).all()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_by_is_printed(is_printed,page, limit):
        try:
            # return OperationalData.query.filter(cast(OperationalData.isPrinted, Boolean) == bool(is_printed)).all()
            offset = (page - 1) * limit
            return (OperationalData.query
                .filter(cast(OperationalData.isPrinted, Boolean) == bool(is_printed))
                .limit(limit)
                .offset(offset)
                .all())
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_by_created_at_range(start_date, end_date):
        try:
            return OperationalData.query.filter(
                and_(OperationalData.created_at >= start_date, OperationalData.created_at <= end_date)
            ).all()
        except SQLAlchemyError as e:
            raise e
        
    @staticmethod
    def getDataById(opId):
        try:
            return OperationalData.query.filter_by(opId=opId).first()
        except SQLAlchemyError as e:
            raise e
    
    @staticmethod
    def getLatestRecord():
        try:
            return OperationalData.query.order_by(OperationalData.created_at.desc()).first()
        except SQLAlchemyError as e:
            raise e
        
    @staticmethod
    def getDistinctAcNo():
        try:
            return OperationalData.query.with_entities(
                cast(OperationalData.ac_no, Integer).label('ac_no_numeric')
            ).distinct().order_by('ac_no_numeric').all()
        except SQLAlchemyError as e:
            raise e
        
    @staticmethod
    def get_all_voter_data_by_ac_no_sl_no():
        try:
            # Retrieve all rows, ordered by ac_no and sl_no
            return OperationalData.query.order_by(OperationalData.ac_no, OperationalData.sl_no).all()
        except SQLAlchemyError as e:
            raise e