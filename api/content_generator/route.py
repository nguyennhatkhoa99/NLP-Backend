import json

from flask import jsonify
from flask_restful import Resource
from api import session
from flask import request

from api.content_generator.model import ContentGeneratorModel

from api.form.service import FormService
from api.content_generator.service import ContentGeneratorService
from api.content_generator import blueprint_api, blueprint
import codecs
import re
@blueprint.route("/")
class ContentGeneratorRoute(Resource):
    
    def get(self, id=None):
        try:
            content_service = ContentGeneratorService()
            if id is not None:
                data = content_service.get(id=id)
               
            data = content_service.get_all()
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
            job = session.query(ContentGeneratorModel).filter_by(id=id).first()
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
            form_id = data["form_id"]
            form =  FormService().get(id=form_id)
            if form["data"] is None:
                raise Exception()
            
            content_service = ContentGeneratorService()
            content, generated_content = content_service.add(data, form_info=form)
            if generated_content:
                content_decoded = codecs.decode(generated_content.content, encoding="utf-8")
                content_decoded = content_decoded.replace("\\n", "<br>").replace("<br><br>", "<br>")
                print(content_decoded)
                update_content = content_service.update(id=content.id, message=content_decoded)
                if update_content:
                    return content_decoded
            return "error"

        
        except Exception as error:
            print(error)
            session.rollback()
            return False

blueprint_api.add_resource(ContentGeneratorRoute, '/content_generator','/content_generator/<string:id>')