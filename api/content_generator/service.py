from api.content_generator.model import ContentGeneratorModel
from api import session
from flask import jsonify
import requests as req
from config import Config
import json

class ContentGeneratorService():
    def add(self,data, form_info=None):
        try:
            content = ContentGeneratorModel(**data)
            content_data = form_info["data"]
            body = {
                "name": content_data["company_name"],
                "domain": content_data["company_field"],
                "website": content_data["company_website"],
                "tone": data["tone"],
                "social_media": data["social_media_type"],
                "startup": False,
                "language": data["language"]
            }
            response = req.post(Config.AI_URL, data=json.dumps(body))
            # if response.status_code == 200:
            #     return 'abc'

            session.add(content)
            
            session.commit()
   
            return content, response
        except Exception as error:
            print(error)
            session.rollback()
            return False
        
    def update(self, id, message=None):
        try:
            job = session.query(ContentGeneratorModel).filter_by(id=id).first()
            if job is None:
                return False
            #job.message = message
            job.content_generate = message
            session.commit()
            session.flush()
            return True 
        except Exception as error:
            print(error)
            session.rollback()
            return False
    
    def get(self, id):
        try:
            job = session.query(ContentGeneratorModel).filter_by(id=id).first()
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
            all_generated_content = session.query(ContentGeneratorModel).all()
            result = []
            for content in all_generated_content:
                result.append()
            return session.query(ContentGeneratorModel).all()
        except Exception as error:
            print(error)
            session.rollback()
            return False
        