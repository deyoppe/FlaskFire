from flask_sqlalchemy import SQLAlchemy
from core import logger

db = SQLAlchemy()

def run():
    logger.debug("Database initialization start")
    
    logger.debug("Database initialized")