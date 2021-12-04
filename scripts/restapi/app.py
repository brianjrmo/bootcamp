# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:26:23 2021

@author: brian
"""
from flask import Flask
from flask import request
from user_management import UserManagement

APP = Flask(__name__)
UM = UserManagement('config.json')

@APP.route('/')
def count():
    '''to check number of active user'''
    return UM.count()

@APP.route('/find', methods=['GET'])
def find():
    '''to find an active user by name'''
    name = request.args.get('username')
    return UM.find(name)

@APP.route('/add', methods=['GET'])
def add():
    '''to add a user'''
    name = request.args.get('username')
    return UM.add(name)

@APP.route('/delete', methods=['GET'])
def delete():
    '''to delete a user by name'''
    name = request.args.get('username')
    return UM.set_status(name, 'DELETED')

@APP.route('/login', methods=['GET'])
def login():
    '''to login with a user'''
    name = request.args.get('username')
    return UM.set_status(name, 'LOGON')

@APP.route('/logoff', methods=['GET'])
def logout():
    '''to logout with a user'''
    name = request.args.get('username')
    return UM.set_status(name, 'LOGOFF')
