import json

from flask import jsonify
from flask_restful import Resource
from api import session
from flask import request

from api.form.model import FormModel
from api.form.service import FormService
from api.form import blueprint_api, blueprint

@blueprint.route("/")
class FormRoute(Resource):
    
    def get(self, id=None):
        try:
            user_service = FormService()
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
            job = session.query(FormModel).filter_by(id=id).first()
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
            form_service = FormService(
                
            )
            form = form_service.add(data)
            if form == True:
                return jsonify(data)

        
        except Exception as error:
            print(error)
            session.rollback()
            return False

blueprint_api.add_resource(FormRoute, '/forms','/form/<string:id>')