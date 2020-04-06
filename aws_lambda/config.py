"""
Implements the configuration related objects.
"""

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    ENGINE = os.environ.get('ENGINE')
    DEBUG = os.environ.get('DEBUG')