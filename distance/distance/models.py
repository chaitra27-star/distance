
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )


DBSession = scoped_session(sessionmaker())
Base = declarative_base()

class Distance( Base):
    __tablename__ = 'distances_shortest'
    _from = Column(String,primary_key=True)
    _to = Column(String,primary_key=True)
    from_name = Column(String)
    to_name = Column(String)
    straight = Column(Float)
    length = Column(Float)
