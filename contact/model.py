# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Index,
    Integer,
    UnicodeText,
    Unicode,
    DateTime,
)

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import register

DBSession = scoped_session(sessionmaker())
register(DBSession)

Base = declarative_base()

__all__ = ['Subject', 'Contact']

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True)

Index('subject_name_index', Subject.name, unique=True)

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey(Subject.id))
    email = Column(Unicode(255), nullable=False)
    text = Column(UnicodeText, nullable=False)
    created = Column(DateTime, default=datetime.now)

Index('contact_email_index', Contact.email)