#!/usr/bin/env python3
"""6. Basic auth class definition"""

from api.v1.auth.auth import Auth
from base64 import b64decode, binascii


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header public methon"""
        if base64_authorization_header is None:
            return None
        if isinstance(base64_authorization_header, str) is False:
            return None
        try:
            decoded_str = b64decode(
                base64_authorization_header.encode('utf-8'))
            return decoded_str.decode('utf-8')
        except binascii.Error:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """extract_user_credentials public method"""
        if decoded_base64_authorization_header is None:
            return None, None
        if isinstance(decoded_base64_authorization_header, str) is False:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':')[:2])
