from api.chat_room.model import ChatroomModel
from api import session

class ChatroomService:
    def __init__(self, session) -> None:
        self.session = session
    
    def add(self,data):
        try:
            user = ChatroomModel(data)
            self.session.add(user)
            self.session.commit()
            return user
        except Exception as error:
            print(error)
            session.rollback()
            return False
        
    def update(self, id, message=None):
        try:
            job = self.session.query(ChatroomModel).filter_by(id=id).first()
            if job is None:
                return False
            job.message = message
            self.session.commit()
            self.session.flush()
            return True 
        except Exception as error:
            print(error)
            session.rollback()
            return False
    
    def get(self, id):
        try:
            job = self.session.query(ChatroomModel).filter_by(id=id).first()
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

    def list(self):
        try:
            return self.session.query(ChatroomModel).all()
        except Exception as error:
            print(error)
            session.rollback()
            return False