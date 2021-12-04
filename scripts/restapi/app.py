from user_management import User_Management
from flask import Flask
from flask import request

app = Flask(__name__)
um = User_Management('config.json')

@app.route('/')
def count():
    return um.count()

@app.route('/find', methods=['GET'])
def find():
    name = request.args.get('username')
    return um.find(name)

@app.route('/add', methods=['GET'])
def add():
    name = request.args.get('username')
    return um.add(name)

@app.route('/delete', methods=['GET'])
def delete():
    name = request.args.get('username')
    return um.set_status(name,'DELETED')
    
@app.route('/login', methods=['GET'])
def login():
    name = request.args.get('username')
    return um.set_status(name,'LOGON')
    
@app.route('/logoff', methods=['GET'])
def logout():
    name = request.args.get('username')
    return um.set_status(name,'LOGOFF')

