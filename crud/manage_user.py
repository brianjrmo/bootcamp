import click
import requests
import json

"""Get from default configuration"""
with open('config.json') as json_file:
    default_conf = json.load(json_file)
    DEFAULT_DOMAIN = default_conf['domain']
    DEFAULT_PORT = default_conf['port']
    
@click.command()
@click.option('--domain', default=DEFAULT_DOMAIN,
              help='(optional) Domain name of the RestFUL API.')
@click.option('--port', default=DEFAULT_PORT,
              help='(optional) Port number of the domain that provide service.')
@click.option('--username', 
              help='User name which you want to manage')
@click.option('--operation', 
              type=click.Choice(['login','logoff','find','add','delete'], 
              case_sensitive=False))
def manage_user(domain, port, username, operation):
    
    if (username==None and operation==None):
        url = "http://{}:{}".format(domain,
                                    port)
        response = requests.get(url)
        print(response.text)    
    elif (username==None or operation==None):
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