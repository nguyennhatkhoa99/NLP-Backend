# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import datetime
from api import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSON
import uuid
from api import session
# from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from sqlalchemy import Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import mapped_column, relationship

class ContentGeneratorModel(Base):

    __tablename__ = 'generated_content'
    
    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    form_id =  mapped_column(UUID(as_uuid=True), ForeignKey('form.id'))
    content_generate = mapped_column(Text())
    tone = mapped_column(String(255))

    def __init__(self, **kwargs):
        print(kwargs)
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]
            setattr(self, property, value)

    def as_dict(self):
        for c in self.__table__.columns:
                print(type(getattr(self, c.name)))
                c.name: str(getattr(self, c.name))
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
    