from logging.config import dictConfig
from datetime import datetime
import logging, sys, os


os.makedirs('logs', exist_ok=True)
logging_config = dict(
    version = 1,
    formatters = {
        'verbose': {
            'format': (
                "[%(asctime)s] %(levelname)s "
                "[%(name)s:%(lineno)s] %(message)s"
            )
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        }
    },
    handlers = {
        'booking_logger': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'level': logging.DEBUG,
            'filename': 'logs/booking_' + datetime.now().strftime("%Y-%m-%d") + '.log',
            'backupCount': 1,  
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': sys.stdout
        }
    },
    loggers = {
        'booking_logger': {
            'handlers': ['booking_logger', 'console'],
            'level': logging.DEBUG
        }
    }
)

dictConfig(logging_config)
booking_logger = logging.getLogger('booking_logger')