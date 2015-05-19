#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table
from sqlalchemy import Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base
import unittest

import dbhelp

class MyTestUnit(unittest.TestCase):
    """class for test the class dbhelp and myapp"""
    def _connect_db(self):
        """connect to database"""
        DB_CONNECT_STRING = "mysql+mysqldb://root:1991719@localhost/myappdb?charset=utf8"
        engine = create_engine(DB_CONNECT_STRING,echo=True)
        Session = sessionmaker()
        Session.configure(bind = engine)
        return Session()

    def setUp(self):
        """insert a user in database for test"""
        session =self._connect_db()
        test_user = dbhelp.User(id =10,name="test")
        session.add(test_user)
        session.commit()
        session.close()
        
    def tearDown(self):
        """destory the user from database"""
        session = self._connect_db()
        user1 = session.query(User).filter(User.id==10).first()
        session.delete(user1)
        session.commit()

    def test_find_value(self):
        """Test for Dbhelper.find_value()"""
        db = dbhelp.Dbhelper()
        session = self._connect_db()
        result = db.find_value(10)
        self.assertEqual(result,'test')
        session.close()
    
    def test_has_key(self):
        """Test for Dbhelper.has_key() """
        db = dbhelp.Dbhelper()
        session = self._connect_db()
        result = db.has_key(10)                  
        self.assertEqual(result,True)
        result = db.has_key(11)                  
        self.assertEqual(result,False)
        session.close()

   # def test_set_key(self):
   #     db = dbhelpe.Dbhelper()
   #     session = self._connect_db()
        

if __name__ == '__main__':
    unittest.main()
