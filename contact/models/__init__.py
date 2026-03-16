from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import register
from sqlalchemy.ext.declarative import declarative_base

DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()

from .mymodel import MyModel
from contact.model import Subject, Contact