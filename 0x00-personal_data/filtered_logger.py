#!/usr/bin/env python3
"""0. Regex-ing 0. Regex-ing"""

import re
import logging
from typing import (
    List,
)
from mysql.connector.connection import MySQLConnection
from os import environ


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        match = r'({}=)([^{}]+)'.format(field, separator)
        message = re.sub(match, r'\1{}'.format(redaction), message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records using filter_datum"""
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))

    logger.addHandler(stream_handler)
    return logger


def get_db() -> MySQLConnection:
    """returns a connector to the database"""
    username = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = environ.get("PERSONAL_DATA_DB_NAME")
    return MySQLConnection(user=username, password=password,
                           host=host, database=db_name)
