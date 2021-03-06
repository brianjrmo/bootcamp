# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:26:23 2021

@author: brian
"""
import datetime
import json
import mysql.connector


class UserManagement():
    """Get initial default config from external file"""
    def __init__(self, config_file):
        with open(config_file) as json_file:
            default_conf = json.load(json_file)
            self.config = default_conf['mysql_conf']

    def _get_user(self, user_name):
        cnx = mysql.connector.connect(**self.config)
        cursor = cnx.cursor()
        query = ("""SELECT * from usertable
                    where name = '{}'
                    and status <> 'DELETED'""".format(user_name))
        cursor.execute(query)
        result = cursor.fetchone()
        cnx.close()
        return result

    def _table_row(self, exclude_status=''):
        cnx = mysql.connector.connect(**self.config)
        cursor = cnx.cursor()
        query = ("""SELECT count(*) from usertable
                    where status <> '{}'""".format(exclude_status))
        cursor.execute(query)
        result = cursor.fetchone()
        cnx.close()
        return result[0]

    def add(self, name):
        """Add user"""
        if self._get_user(name) is not None:
            message = "User already exist."
            return_code = 400
        else:
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()
            _id = self._table_row()
            last_action = datetime.datetime.now()
            query = ("INSERT INTO mysql.usertable VALUE(%s,%s,'LOGOFF',%s)")
            cursor.execute(query, (_id, name, last_action))
            cnx.commit()
            cnx.close()
            message = "User {} added".format(name)
            return_code = 200
        return message, return_code

    def count(self):
        """Count number of user"""
        count = self._table_row(exclude_status='DELETED')
        if count == 0:
            message = "There is no user."
        elif count == 1:
            message = "There is 1 user."
        else:
            message = "There are {} users.".format(count)
        return message

    def find(self, name):
        """find user by name"""
        if self._get_user(name) is None:
            message = "User not found."
            return_code = 400
        else:
            message = "User found."
            return_code = 200
        return message, return_code

    def set_db_host(self, hostname):
        """set db host name if it's not default"""
        self.config['host'] = hostname

    def set_status(self, name, status):
        """set user status"""
        if self._get_user(name) is None:
            message = "User not exist."
            return_code = 400
        else:
            cnx = mysql.connector.connect(**self.config)
            cursor = cnx.cursor()
            last_action = datetime.datetime.now()
            query = ("""UPDATE mysql.usertable
                        set status = '{}',
                            last_action = '{}'
                        where name = '{}'
                        and   status<>'DELETED'""".format(status,
                                                          last_action,
                                                          name))
            cursor.execute(query)
            cnx.commit()
            cnx.close()
            message = "User {} {}".format(name, status)
            return_code = 200
        return message, return_code
