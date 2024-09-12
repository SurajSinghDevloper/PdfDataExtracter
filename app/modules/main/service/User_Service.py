from app.modules.main.models.User_Model import User_Model
from app.db.db import db
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash
from app.modules.main.models.Role import Role
from app.modules.main.models.UserRoles import User_Role

class UserService:

    @staticmethod
    def create_user(data):
        try:
            hashed_password = generate_password_hash(data['password'])
            role = Role.query.filter_by(name='USERS').first()
            if not role:
             raise ValueError(f"Role 'name='USERS'' not found.")
            new_user = User_Model(
                name=data['name'],
                email=data['email'],
                mobile=data['mobile'],
                password=hashed_password, 
                dob=data['dob']
            )
            db.session.add(new_user)
            db.session.commit()
            newRole = User_Role(
                user_id=new_user.id,
                role_id=role.id
            )
            db.session.add(newRole)
            db.session.commit()
            return new_user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_user_by_id(user_id):
        return User_Model.query.get(user_id)
    
    @staticmethod
    def verify_password(stored_password, provided_password):
        return check_password_hash(stored_password, provided_password)

    @staticmethod
    def get_user_by_email(email):
        return User_Model.query.filter_by(email=email).first()
    
    @staticmethod
    def get_all_users():
        return User_Model.query.all()

    @staticmethod
    def update_user(user_id, data):
        user = User_Model.query.get(user_id)
        if user:
            try:
                user.name = data['name']
                user.email = data['email']
                user.mobile = data['mobile'] 
                user.dob = data['dob']
                db.session.commit()
                return user
            except SQLAlchemyError as e:
                db.session.rollback()
                raise e
        return None

    @staticmethod
    def delete_user(user_id):
        user = User_Model.query.get(user_id)
        if user:
            try:
                db.session.delete(user)
                db.session.commit()
                return True
            except SQLAlchemyError as e:
                db.session.rollback()
                raise e
        return False

    @staticmethod
    def role_by_userid(userid):
        user_roles = db.session.query(User_Role).filter_by(user_id=userid).all()
        role_ids = [user_role.role_id for user_role in user_roles]
        roles = db.session.query(Role).filter(Role.id.in_(role_ids)).all()
        
        # Convert roles to a serializable format
        serializable_roles = [role.to_dict() for role in roles]
        
        print("USER ROLES ====>", serializable_roles)
        
        return serializable_roles

