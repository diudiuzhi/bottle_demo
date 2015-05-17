from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table
from sqlalchemy import Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class user(Base):
    __tablename__ ='user'
    id = Column(Integer,primary_key=True)
    name = Column(String(20),nullable=False)

class dbhelper():
    def __init__(self):
        DB_CONNECT_STRING="mysql+mysqldb://root:1991719@localhost/myappdb?charset=utf8"
        self.engine = create_engine(DB_CONNECT_STRING,echo=True)
        self.Session = sessionmaker()
        self.Session.configure(bind = self.engine)
        
    def find_value(self,key):
        session = self.Session()
        result  = session.query(user).filter(user.id == key).first()
        session.close()
        if result == None:
            return None
        value = result.name
        return value
   
    def has_key(self,key):
        session = self.Session()
        result = session.query(user).filter(user.id == key).first()
        session.close()
        if result == None:
            return False
        return True

    def set_value(self,key,value):
        session = self.Session()
        m_user = user(id=key,name=value)
        session.add(m_user)
        session.commit()
        session.close() 
                

#db=dbhelper()
#Base.metadata.reflect(db.engine)
#Base.metadata.create_all(db.engine)








