from core import logger, app, constants
from flask_sqlalchemy import SQLAlchemy
from os import path
import glob
import importlib
db = SQLAlchemy()

def run():    
    logger.debug("Database initialization start")       

    model_dir = path.join(constants.MODELS_PATH, "*.py")
    logger.debug("Loading all models in directory: {:s}".format(model_dir))
    
    model_files = glob.glob(model_dir)
    logger.debug("Found models: {:s}".format(str(model_files)))

    models = [ path.basename(f)[:-3] for f in model_files if path.isfile(f)]
    for model in models:
        __register_model(model)
        
    db.init_app(app)

    logger.debug("Database initialized")
    
def __register_model(model):
    module_name = "app.models.{:s}".format(model)
    logger.info("Loading model: {:s}".format(model))
    
    importlib.import_module(module_name)