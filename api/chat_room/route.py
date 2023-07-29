import json

from flask_restful import Resource
from api import session
from flask import request

from api.chat_room.model import ChatroomModel
from api.chat_room import blueprint_api, blueprint
from api.chat_room.service import ChatroomService

@blueprint.route("/")
class ChatroomRoute(Resource):

    def get(self, id):
        try:
            data = ChatroomService.get(id)
            return {
                "data": data.as_dict(),
                "status": "success",
                "message": "Get job successfully!"
            }
        except Exception as error:
            return {
                "data": None,
                "status": "error",
                "message": str(error)
            }
        
    def put(self, id):
        try:
            data = request.json
            status = data["status"]
            message = data["message"]
            job = session.query(ChatroomModel).filter_by(id=id).first()
            if job is None:
                return False
            job.status = status
            job.message = message
            session.commit()
            session.flush()
            return True 
        except Exception as error:
            print(error)
            session.rollback()
            return False
        
    
    def get(self):
        try:
            data = ChatroomService.list()
            return {
                "data": data.as_dict(),
                "status": "success",
                "message": "Get job successfully!"
            }
        except Exception as error:
            return {
                "data": None,
                "status": "error",
                "message": str(error)
            }
        
    def post(self):
        try:
            data = request.json
            
        
        except Exception as error:
            print(error)
            session.rollback()
            return False
   
blueprint_api.add_resource(ChatroomRoute, '/chat/<string:id>')