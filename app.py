"""
import logging
import subprocess, sys
import time
import socket
import os
import uuid



FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
d = {'clientip': socket.gethostname(), 'uid': os.getuid()}
logging.basicConfig(format=FORMAT)
logs = logging.getLogger('__name__')
logs.warning(msg='starting process', extra=d)






time.sleep(5)
"""
import configparser
import logging
from jinja2 import Template



LOGGING_NAME = "Deployment"
def get_configuration():
    pass

def setup():
    pass

def get_deployment():
    pass

def transfer_powershell(config):
    filename = config.get('filename')

    if filename:
        with open(filename, 'r') as f:
            cxt = f.read()
        with open('./power-scheduler/power_scheduler/templates/template.txt', 'r') as f:
            template = Template(f.read())
        with open('./power-scheduler/power_scheduler/__main__.py', 'w') as f:
            f.writelines(template.render(powershell=cxt))

# Creates the docker client

if __name__ == "__main__":
    #logging.getLogger(LOGGING_NAME)
    #get_configuration()
    #setup()
    #get_deployment()
    transfer_powershell({"filename":"Script_ProcessTabularModel.ps1"})


