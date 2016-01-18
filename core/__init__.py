# Order is important
from core.system.constants import constants
from core.system.app import app
from core.system.logger import logger
from core.system.db import db


def run():
    import core.system.db as _db
    import core.system.app as _app
    
    logger.fatal("Core run start")
    _db.run()
    _app.run()
    logger.debug("Core run completed")