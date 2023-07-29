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
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from api.user.model import UserModel

class ChatroomModel(Base):

    __tablename__ = 'chatroom'
    
    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = mapped_column(String(64))
    creator_id = mapped_column(ForeignKey('user.id'))
    created_at = mapped_column(DateTime, default=datetime.datetime.now)
    updated_at = mapped_column(DateTime, default=datetime.datetime.now)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]
            setattr(self, property, value)

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}