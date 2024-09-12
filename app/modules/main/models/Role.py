from app.db.db import db
from sqlalchemy import event
from sqlalchemy.orm import Session

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    status = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'<Role {self.id}>'
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status
        }
# Move the event listener outside the class definition
# @event.listens_for(Role.__table__, 'after_create')
# def insert_initial_roles(*args, **kwargs):
#     session = Session(db.engine)
#     session.add_all([
#         Role(name='USERS', status="ACTIVE"),
#         Role(name='ADMIN', status="ACTIVE"),
#         Role(name='GUEST', status="ACTIVE")
#     ])
#     session.commit()
#     session.close()
