from app.db.db import db

class OperationalData(db.Model):
    __tablename__ = 'operational_data'
    
    opId = db.Column(db.Integer, primary_key=True,autoincrement=True)
    date = db.Column(db.DateTime)
    id = db.Column(db.Integer)
    barcode_no = db.Column(db.String(255))
    id_no = db.Column(db.String(255))
    form_ref_no = db.Column(db.String(255))
    sub_id = db.Column(db.String(255))
    name = db.Column(db.String(355))
    father_name = db.Column(db.String(355))
    monther_name=db.Column(db.String(255))
    husband_name=db.Column(db.String(255))
    wife_name=db.Column(db.String(255))
    other_gurdian=db.Column(db.String(255)) 
    address = db.Column(db.Text)
    district = db.Column(db.String(255))
    mobile_no = db.Column(db.String(15), nullable=True)
    state_code = db.Column(db.String(10))
    ac_no = db.Column(db.String(10))
    part_no = db.Column(db.String(10))
    sl_no = db.Column(db.String(10))
    filename = db.Column(db.Text)
    uploadedBy =db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    isPrinted =db.Column(db.Boolean,default=False)
    printedBy = db.Column(db.Integer)
    # page_no=db.Column(db.Integer)
    # sticker_no = db.Column(db.Integer,default=0)
    lot_no=db.Column(db.String(255),default=0)
    printCount = db.Column(db.Integer,default=False)
    
    
    
    
    def __repr__(self):
        return f'<OperationalData {self.name}>'
    
    
    def serialize(self):
        return {
            'opId': self.opId,
            'date': self.date.isoformat(), 
            'id': self.id,
            'barcode_no': self.barcode_no,
            'id_no': self.id_no,
            'form_ref_no': self.form_ref_no,
            'sub_id': self.sub_id,
            'name': self.name,
            'father_name': self.father_name,
            'monther_name':self.monther_name,
            'husband_name':self.husband_name,
            'wife_name':self.wife_name,
            'other_gurdian':self.other_gurdian,
            'address': self.address,
            'district':self.district,
            'mobile_no': self.mobile_no,
            'state_code': self.state_code,
            'ac_no': self.ac_no,
            'part_no': self.part_no,
            'sl_no': self.sl_no,
            'filename': self.filename,
            'uploadedBy': self.uploadedBy,
            'created_at': self.created_at.isoformat(),  # Convert datetime to ISO format string
            'isPrinted': self.isPrinted,
            'printedBy': self.printedBy,
            # 'page_no':self.page_no,
            # 'sticker_no':self.sticker_no,
            'lot_no':self.lot_no,
            'printCount': self.printCount
        }