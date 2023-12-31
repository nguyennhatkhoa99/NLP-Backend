import json

from flask import jsonify
from flask_restful import Resource
from api import session
from flask import request

from api.user.model import UserModel
from api.user.service import UserService
from api.user import blueprint_api, blueprint

@blueprint.route("/")
class UserRoute(Resource):
    
    def get(self, id=None):
        try:
            user_service = UserService()
            if id is not None:
                data = user_service.get(id=id)
               
            data = user_service.get_all()
            return {
                    "data": data,
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
            job = session.query(UserModel).filter_by(id=id).first()
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
        
    def post(self, id=None):
        try:
            data = request.json
            user_service = UserService()
            user = user_service.add(data)
            if user == True:
                return jsonify(data)

        
        except Exception as error:
            print(error)
            session.rollback()
            return False

blueprint_api.add_resource(UserRoute, '/users','/user/<string:id>')