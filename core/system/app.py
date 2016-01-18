# App imports
from flask import Flask
from core import constants

# System imports
from os import path
import importlib
import glob

# Init
app = Flask(__name__)
logger = app.logger

def run():
    logger.debug("App initialization start")
    
    controller_dir = path.join(constants.CONTROLLERS_PATH, "*.py")
    logger.debug("Loading all controllers in directory: {:s}".format(controller_dir))
    
    controller_files = glob.glob(controller_dir)
    logger.debug("Found controllers: {:s}".format(str(controller_files)))

    controllers = [ path.basename(f)[:-3] for f in controller_files if path.isfile(f)]
    for controller in controllers:
        __register_controller(controller)
        
    app.run()
            
    logger.debug("App initialized")
    
def __register_controller(controller):
    module_name = "app.controllers.{:s}".format(controller)
    logger.info("Registering controller: {:s}".format(controller))
    
    module = getattr(importlib.import_module(module_name), "controller")
    url_prefix = "/{:s}".format(controller)
    app.register_blueprint(module, url_prefix=url_prefix)
    logger.info("Controller {:s} registered at {:s}".format(controller, url_prefix))