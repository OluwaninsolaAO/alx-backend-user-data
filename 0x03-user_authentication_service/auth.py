#!/usr/bin/env python3
"""Auth Module, defining helper function such as _hash_pw"""
from bcrypt import gensalt, hashpw


def _hash_password(password: str) -> bytes:
    """4. Hash password with bcrypt"""
    return hashpw(password.encode('utf-8'), gensalt())
