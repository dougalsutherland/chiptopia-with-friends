import logging
from logging.handlers import SMTPHandler
import sys

from .default import *

DEBUG = False


logging.basicConfig(stream=sys.stderr)
mail_handler = SMTPHandler('127.0.0.1', 'ptv@dougal.me', ADMINS,
                           "[chips] blew up")
mail_handler.setLevel(logging.ERROR)
LOG_HANDLERS = [mail_handler]
