#!/usr/bin/env python3
"""6. Basic auth class definition"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic API authentication"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """extract_base64_authorization_header public method"""
        if authorization_header is None:
            return None
        if isinstance(authorization_header, str) is False:
            return None
        if authorization_header.split()[0] != 'Basic':
            return None
        return ''.join(authorization_header.split()[1:])
