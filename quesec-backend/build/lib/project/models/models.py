# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

import datetime

from sqlalchemy import Column, Integer, String, Date

from project.models.init_db import db

class DeviceConnector(db.Model):
    """Device Connector Model"""
    __tablename__ = 'deviceconnector'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    created_date = Column(Date, default=datetime.datetime.now)
    inputxml = Column(String, nullable=False)
    outputxml = Column(String, nullable=False)
