import core.constants as _constants
constants = _constants

import core.app as _app
app = _app.app

import core.logger as _logger
logger = _logger.logger

import core.db as _db
db = _db.db

def run():
    logger.fatal("Core run start")
    _app.run()
    _db.run()
    logger.debug("Core run completed")