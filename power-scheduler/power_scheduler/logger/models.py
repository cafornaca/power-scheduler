from sqlalchemy import Column
from sqlalchemy.types import DATETIME, BIGINT, VARCHAR
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Log(Base):
    __tablename__ = 'MODEL_BATCH_LOGS'
    id = Column(BIGINT, primary_key=True) # auto incrementing
    logger = Column(VARCHAR) # the name of the logger. (e.g. myapp.views)
    level = Column(VARCHAR) # info, debug, or error?
    trace = Column(VARCHAR) # the full traceback printout
    msg = Column(VARCHAR) # any custom log you may have included
    created_at = Column(DATETIME, default=func.now()) # the current timestamp

    def __init__(self, logger=None, level=None, trace=None, msg=None):
        self.logger = logger
        self.level = level
        self.trace = trace
        self.msg = msg

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "<Log: %s - %s>" % (self.created_at.strftime('%m/%d/%Y-%H:%M:%S'), self.msg[:50])

    def add(self, session):
        """
        A function to save the ORM object to the database .
        """
        session.add(self)
        return self.to_dict()

    def to_dict(self):
        """
        A function to transform the ORM object to a dictionary.
        """
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}