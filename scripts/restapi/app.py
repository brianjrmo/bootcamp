import datetime
import mysql.connector
from flask import Flask
from flask import request

app = Flask(__name__)
config = {
  'user': 'bootcamp',
  'password': 'bootcamp',
  'host': 'bootcamp_mysql',
  'database': 'mysql',
  'raise_on_warnings': True
}

def table_row(exclude_status=''):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("""SELECT count(*) from usertable 
                where status <> '{}'"""
             .format(exclude_status))
    cursor.execute(query)
    result=cursor.fetchone()
    cnx.close()
    return result[0]

def get_user(user_name):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("""SELECT * from usertable 
                where name = '{}' 
                and status <> 'DELETED'"""
                .format(user_name))
    cursor.execute(query)
    result = cursor.fetchone()
    cnx.close()
    return result

@app.route('/')
def user_count():
    count = table_row(exclude_status='DELETED')
    if count == 0:
        message = "There is no user."
    elif count == 1:
        message = "There is 1 user."
    else:
        message = "There are {} users.".format(count)
    return message


@app.route('/find', methods=['GET'])
def find():
    name = request.args.get('username')
    return _find(name)

def _find(name):
    if get_user(name) == None:
        message = "User not found."
    else:
        message = "User found."
    return message

@app.route('/add', methods=['GET'])
def add():
    name = request.args.get('username')
    return _add(name)

def _add(name):
    if get_user(name) != None:
        message = "User already exist."
        return_code = 400
    else:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        id = table_row()
        last_action = datetime.datetime.now()
        query = ("INSERT INTO mysql.usertable VALUE(%s,%s,'LOGOFF',%s)")
        cursor.execute(query,(id, name, last_action))
        cnx.commit()
        cnx.close()
        message = "User {} added".format(name)
        return_code = 200
    return message, return_code

@app.route('/delete', methods=['GET'])
def delete():
    name = request.args.get('username')
    return _set_status(name,'DELETED')
    
@app.route('/login', methods=['GET'])
def login():
    name = request.args.get('username')
    return _set_status(name,'LOGON')
    
@app.route('/logoff', methods=['GET'])
def logout():
    name = request.args.get('username')
    return _set_status(name,'LOGOFF')

def _set_status(name,status):
    if get_user(name) == None:
        message = "User not exist."
        return_code = 400
    else:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        last_action = datetime.datetime.now()
        query = ("""UPDATE mysql.usertable 
                    set status = '{}', 
                        last_action = '{}'
                    where name = '{}'
                    and   status<>'DELETED'"""
                    .format(status,last_action,name))
        cursor.execute(query)
        cnx.commit()
        cnx.close()
        message = "User {} {}".format(name,status)
        return_code = 200
    return message, return_code