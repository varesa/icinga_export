import sys
sys.path.insert(0, "/var/www/icinga_export")

from icinga_export import app as application

import logging, logging.handlers
log = logging.handlers.RotatingFileHandler("/var/log/icinga-export/application.log")
log.setLevel(logging.DEBUG)
application.logger.addHandler(log)