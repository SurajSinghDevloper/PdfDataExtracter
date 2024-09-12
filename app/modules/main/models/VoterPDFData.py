from app.db.db import db
from datetime import datetime

class VoterPdfData_Model(db.Model):
    __tablename__ = 'voter_pdf_data'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    barcode_no = db.Column(db.String(255))
    id_no = db.Column(db.String(255))
    form_ref_no = db.Column(db.String(255))
    sub_id = db.Column(db.String(255))
    name = db.Column(db.String(255))
    father_name = db.Column(db.String(255))
    monther_name=db.Column(db.String(255))
    husband_name=db.Column(db.String(255))
    wife_name=db.Column(db.String(255))
    other_gurdian=db.Column(db.String(255)) 
    address = db.Column(db.Text)
    district = db.Column(db.String(255))
    mobile_no = db.Column(db.String(15))
    state_code = db.Column(db.String(10))
    ac_no = db.Column(db.String(10))
    part_no = db.Column(db.String(10))
    sl_no = db.Column(db.String(10))
    filename = db.Column(db.String(255))
    lot_no=db.Column(db.String(255),default=0)
    uploadedBy =db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<VoterPdfData_Model {self.name}>'