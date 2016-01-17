from flask import Flask
from os import path
from core.constants import directory
import logging
import importlib
import glob
app = Flask(__name__)
app.debug = True

def run():
    app.logger.info("Run start")
    init_app()
    app.logger.info("Run end")
    
def init_logger():
    app.logger.setLevel(logging.DEBUG)
    
def init_app():
    app.logger.info("App: starting")
    
    controller_dir = path.join(directory["controllers"], "*.py")
    app.logger.debug("Loading all controllers in directory: {:s}".format(controller_dir))
    
    controller_files = glob.glob(controller_dir)
    app.logger.debug("Found controllers: {:s}".format(str(controller_files)))
    
    controllers = [ path.basename(f)[:-3] for f in controller_files if path.isfile(f)]
    for controller in controllers:
        module_name = "app.controllers.{:s}".format(controller)
        app.logger.info("Registering controller: {:s}".format(controller))
        
        module = getattr(importlib.import_module(module_name), "controller")
        app.register_blueprint(module, url_prefix="/{:s}".format(controller))
        app.logger.info("Registration of controller {:s} completed".format(controller))
        
    app.run()
    app.logger.info("App: start completed")