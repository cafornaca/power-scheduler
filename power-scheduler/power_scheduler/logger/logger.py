import logging
import traceback
import sqlalchemy
from sqlalchemy import orm
from logger.models import Log
from datetime import datetime



class SQLAlchemyHandler(logging.Handler):
    
    def __init__(self, session):
        super().__init__()
        self.session = session

    def emit(self, record):
        trace = None
        exc = record.__dict__['exc_info']
        if exc:
            trace = traceback.format_exc()
        log = Log(
            logger=record.__dict__['name'],
            level=record.__dict__['levelname'],
            trace=trace,
            msg=record.__dict__['msg'],)
        self.session.add(log)
        self.session.commit()

    
    