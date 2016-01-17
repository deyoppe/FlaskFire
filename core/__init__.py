from flask import Flask
from os import path
from core.constants import directory
import logging
import importlib
import glob
app = Flask(__name__)
logger = app.logger

def run():
    logger.debug("Core run start")
    __init_app()
    logger.debug("Core run completed")

def __init_app():
    logger.debug("App initialization start")
    
    controller_dir = path.join(directory["controllers"], "*.py")
    logger.debug("Loading all controllers in directory: {:s}".format(controller_dir))
    
    controller_files = glob.glob(controller_dir)
    logger.debug("Found controllers: {:s}".format(str(controller_files)))
    
    controllers = [ path.basename(f)[:-3] for f in controller_files if path.isfile(f)]
    for controller in controllers:
        module_name = "app.controllers.{:s}".format(controller)
        logger.info("Registering controller: {:s}".format(controller))
        
        module = getattr(importlib.import_module(module_name), "controller")
        url_prefix = "/{:s}".format(controller)
        app.register_blueprint(module, url_prefix=url_prefix)
        logger.info("Controller {:s} registered at {:s}".format(controller, url_prefix))
        
    app.run()
    logger.debug("App initialized")