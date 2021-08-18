#!/usr/bin/env python3
""" User model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
""" import flask after building a package"""
Base = declarative_base()


class User(Base):
    """ SQLAlchemy models for table named users """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
