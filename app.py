#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route,run,request,abort
import dbhelp

@route('/')
def index():
    return ''' <form action="/GetValue" method="get">
               Get Value: <input name="key" type="text"/>
               <input value="Get" type="submit">
               </form>
           '''
db = dbhelp.Dbhelper()

@route ('/GetValue',method='GET')
def getValue():
    '''Get the key from '/'.If the key has existed in database,return
       the value,else return 404 '''
    key = request.query.key                  
    result = db.find_value(key)
    if result != None:
        return key + ": "+result
    return abort(404,'Resource does not exist')

@route ('/SetValue',method='POST')
def setValue():
    '''Set the K-V with json. If the data not belong json,return 400.
       If the key has existed,return 419. If not existed ,set database and
       return the json value'''
    if request.content_type != "application/json":
        return abort(400,'Not Json')
    result = request.json
    key =  result['id']
    value = result['name']
    isExist = db.has_key(key)
    if isExist:
        return abort(419,'key has existed')
    else:
        db.set_value(key,value) 
    return result

run(host='10.166.224.13',port=8080)
