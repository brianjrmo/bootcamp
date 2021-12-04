# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:26:23 2021

@author: brian
"""
# pylint: disable=no-value-for-parameter
import json
import click
import requests

#Get from default configuration
with open('config.json') as json_file:
    DEFAULT_CONF = json.load(json_file)
    DEFAULT_DOMAIN = DEFAULT_CONF['domain']
    DEFAULT_PORT = DEFAULT_CONF['port']

@click.command()
@click.option('--domain', default=DEFAULT_DOMAIN,
              help='(optional) Domain name of the RestFUL API.')
@click.option('--port', default=DEFAULT_PORT,
              help='(optional) Port number of the domain that provide service.')
@click.option('--username',
              help='User name which you want to manage')
@click.option('--operation',
              type=click.Choice(['login', 'logoff', 'find', 'add', 'delete'],
                                case_sensitive=False)
              )
def manage_user(domain, port, username, operation):
    """Manage user by call-in name and necessary function"""
    if (username is None and operation is None):
        url = "http://{}:{}".format(domain,
                                    port)
        response = requests.get(url)
        print(response.text)
    elif (username is None or operation is None):
        print("username and operation are mandate.",
              "type in 'python manage_user.py --help' to get more information")
    else:
        url = "http://{}:{}/{}?username={}".format(domain,
                                                   port,
                                                   operation.lower(),
                                                   username)
        response = requests.get(url)
        print(response.text)


if __name__ == '__main__':
    manage_user()
