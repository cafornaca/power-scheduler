import docker
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
        with open('./templates/template.txt', 'r') as f:
            template = Template(f.read())
        with open('./power-scheduler/power_scheduler/__main__.py', 'w') as f:
            f.writelines(template.render(powershell=cxt))

# Creates the docker client
client = docker.from_env()

if __name__ == "__main__":
    #logging.getLogger(LOGGING_NAME)
    #get_configuration()
    #setup()
    #get_deployment()
    transfer_powershell({"filename":"Script_ProcessTabularModel.ps1"})