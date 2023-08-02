#!/usr/bin/env python3
"""0. Regex-ing 0. Regex-ing"""

import re
from typing import (
    List,
)


def filter_datum(fields: List, redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        match = r'({}=)([^{}]+)'.format(field, separator)
        message = re.sub(match, r'\1{}'.format(redaction), message)
    return message
