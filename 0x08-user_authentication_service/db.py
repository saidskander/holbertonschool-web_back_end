#!/usr/bin/env python3
""" session, add, find, update, Create user, Find user, Update user """
from user import Base, User
from typing import TypeVar
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """ class """
    def __init__(self):
        """ SQL engine db constructor """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ Create a session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ save the user to the database and returns a User object """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ returns the first row found in the users table """
        if kwargs is None:
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        else:
            return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        locate the user using find_user_by,
        then update the user’s attributes
        then commit changes to the database
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError
            else:
                setattr(user, key, value)
        self._session.commit()
