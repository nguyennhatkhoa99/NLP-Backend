from api.form.model import FormModel
from api import session
from flask import jsonify

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
            return True
        except Exception as error:
            print(error)
            session.rollback()
            return False
        
    def update(self, id, message=None):
        try:
            job = session.query(FormModel).filter_by(id=id).first()
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
            return session.query(FormModel).all()
        except Exception as error:
            print(error)
            session.rollback()
            return False
        