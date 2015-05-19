#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table
from sqlalchemy import Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """ A class for mapping between user class and database """
    __tablename__ ='user'
    id = Column(Integer,primary_key=True)
    name = Column(String(20),nullable=False)

class Dbhelper():
    """A wrapper for mysql"""
    def __init__(self):
        """connect the mysql"""
        DB_CONNECT_STRING="mysql+mysqldb://root:1991719@localhost/myappdb?charset=utf8"
        self.engine = create_engine(DB_CONNECT_STRING,echo=True)
        self.Session = sessionmaker()
        self.Session.configure(bind = self.engine)
        
    def find_value(self,key):
        """use the key to find in database and return the value"""
        session = self.Session()
        result  = session.query(User).filter(User.id == key).first()
        session.close()
        if result == None:
            return None
        value = result.name
        return value
   
    def has_key(self,key):
        """judge whether the key has existed in database,if exist,return True. 
           Not,return False"""
        session = self.Session()
        result = session.query(User).filter(User.id == key).first()
        session.close()
        if result == None:
            return False
        return True

    def set_value(self,key,value):
        """insert k-v in database"""
        session = self.Session()
        m_user = User(id=key,name=value)
        session.add(m_user)
        session.commit()
        session.close() 
                

#db=dbhelper()
#Base.metadata.reflect(db.engine)
#Base.metadata.create_all(db.engine)








