from app.db.db import db

class User_Role(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,  nullable=False)
    role_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User_Role {self.id}>'