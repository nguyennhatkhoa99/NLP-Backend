from api.user.model import UserModel
from api import session
from flask import jsonify

class UserService():
    def add(self,data):
        try:
            user = UserModel(**data)
            session.add(user)
            session.commit()
            return True
        except Exception as error:
            print(error)
            session.rollback()
            return False
        
    def update(self, id, message=None):
        try:
            job = session.query(UserModel).filter_by(id=id).first()
            if job is None:
                return False
            job.message = message
            session.commit()
            session.flush()
            return True 
        except Exception as error:
            print(error)
            session.rollback()
            return False
    
    def get(self, id):
        try:
            job = session.query(UserModel).filter_by(id=id).first()
            return {
                "data": job.as_dict(),
                "status": "success",
                "message": "Get job successfully!"
            }
        except Exception as error:
            return {
                "data": None,
                "status": "error",
                "message": str(error)
            }

    def get_all(self):
        try:
            return session.query(UserModel).all()
        except Exception as error:
            print(error)
            session.rollback()
            return False
        