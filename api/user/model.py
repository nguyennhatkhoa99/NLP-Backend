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
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
# from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import mapped_column, relationship

class UserModel(Base):

    __tablename__ = 'user'
    
    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    phone = mapped_column(String(16))
    email = mapped_column(String(255))
    password = mapped_column(String(40))
    first_name = mapped_column(String(20))
    last_name = mapped_column(String(20))
    chatrooms = relationship("ChatroomModel", backref="user")
    is_active = mapped_column(Boolean, unique=False, default=False)
    is_authenticate = mapped_column(Boolean,default=False)
    created_at = mapped_column(DateTime, default=datetime.datetime.now)
    updated_at = mapped_column(DateTime, default=datetime.datetime.now)

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
    
class Role(Base):
    __tablename__ = 'role'
    id = mapped_column(Integer(), primary_key=True)
    name = mapped_column(String(80), unique=True)
    description = mapped_column(String(255))

    def __repr__(self):
        return '<Role(%s, %s)>' % (self.id, self.name)
