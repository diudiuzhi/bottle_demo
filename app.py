from bottle import route,run,request,abort
import dbhelp

@route('/')

def index():
    return ''' <form action="/GetValue" method="get">
               Get Value: <input name="key" type="text"/>
               <input value="Get" type="submit">
               </form>
           '''
db = dbhelp.dbhelper()

@route ('/GetValue',method='GET')

def getValue():
    key = request.query.key   #Get the Key of user input
    result = db.find_value(key)
    if result != None:
        return key + ": "+result
    return abort(404,'Resource does not exist')

@route ('/SetValue',method='POST')

def setValue():
    if request.content_type != "application/json":
        return abort(400,'Not Json')
    #print request.json
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
