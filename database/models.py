from sqlalchemy import Column, String, Integer, Date, DateTime, Text

from .database import Base



    

""" For base database"""

class Cluster(Base):
    __tablename__ = 'cluster'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))
    description = Column(String(255))
    
    
class Broker(Base):
    __tablename__ = 'broker'
    
    id = Column(Integer, primary_key=True, index=True)
    cluster_id = Column(Integer)
    name = Column(String(45))
    server = Column(String(45))
    description = Column(String(45))
    

class Topic(Base):
    __tablename__ = 'topic'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))
    cluster_id = Column(Integer)
    description = Column(String(255))
    

""" For recognition database """

class Recognite(Base):
    __tablename__ = 'recognite'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))
    source_topic = Column(Integer)
    destination_topic = Column(Integer)