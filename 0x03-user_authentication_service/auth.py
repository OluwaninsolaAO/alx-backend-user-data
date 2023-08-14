#!/usr/bin/env python3
"""Auth Module, defining Auth class"""
from db import DB
from bcrypt import gensalt, hashpw, checkpw
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """4. Hash password with bcrypt"""
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    """9. Generate UUIDs with uuid4"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Awesome Auth Class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new User in database"""
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                raise ValueError('User {} already exists'.format(
                    email))
        except NoResultFound:
            return self._db.add_user(email,
                                     hashed_password=_hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validates login credentials"""
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'),
                           user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """10. Get session ID"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
