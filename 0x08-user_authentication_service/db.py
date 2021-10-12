#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """ DB class """

    def __init__(self):
        """ Instance """

        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ Sets up session """

        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Create user in to db """

        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """ Returns the first row found in the users table """

        if not kwargs:
            raise InvalidRequestError

        users_columns = [
            'id',
            'email',
            'hashed_password',
            'session_id',
            'reset_token'
        ]

        for arg in kwargs:
            if arg not in users_columns:
                raise InvalidRequestError

        search_user = self._session.query(User).filter_by(**kwargs).first()

        if search_user:
            return search_user
        else:
            raise NoResultFound
