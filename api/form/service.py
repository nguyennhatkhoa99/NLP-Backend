from api.form.model import FormModel
from api import session
from flask import jsonify
import json

class FormService():
    company_name: str
    company_website : str
    company_field: str


    def __init__(self, 
                company_name="",
                company_website="",
                company_field= "",
                company_description="",
                target_audience="",
                company_social_link=""
                ):
        self.company_name = company_name
        self.company_website = company_website
        self.company_field = company_field
        self.company_description = company_description
        self.target_audience = target_audience
        self.company_social_link = company_social_link

    def add(self,data):
        try:
            form = FormModel(**data)
            session.add(form)
            session.commit()
            return {
                "status": 200,
                "id": form.id,
                "message": "Form create success"
            }
        except Exception as error:
            print(error)
            session.rollback()
            return False
        
    def update(self, id, data):
        try:
            form = session.query(FormModel).filter_by(id=id).first()
            if form is None:
                return False
            form.company_name = data.company_name
            form.company_website = data.company_website
            form.company_field = data.company_field
            form.company_description = data.company_description
            session.commit()
            session.flush()
            return True 
        except Exception as error:
            print(error)
            session.rollback()
            return False
    
    def get(self, id):
        try:
            form = session.query(FormModel).filter_by(id=id).first()
            
            return {
                "data": form.as_dict(),
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
            all_form = session.query(FormModel).all()
            result  = []
            for form in all_form:
                result.append(form.as_dict())
            print(result)
            return result
        except Exception as error:
            print(error)
            session.rollback()
            return False
    
    # def soft_delete(self, id=None):
    #     try:
    #         form = session.query(FormModel).filter_by(id=id).first()
            
    #     except: Exception as error