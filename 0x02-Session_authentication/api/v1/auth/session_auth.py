#!/usr/bin/env python3
"""0x02. Session authentication"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Session Authentication Definition"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session for a User with the user_id"""
        if any([user_id is None, not isinstance(user_id, str)]):
            return None
        session_id = uuid4().__str__()
        self.user_id_by_session_id.update({session_id: user_id})
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns user_id based associated with the session_id"""
        if any([session_id is None, not isinstance(session_id, str)]):
            return None
        return self.user_id_by_session_id.get(session_id, None)
