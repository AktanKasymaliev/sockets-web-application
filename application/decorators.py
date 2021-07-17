import functools
from application.logger_cfg import LoggingConfig

logger = LoggingConfig(__name__)

def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.log.error(e)
    return wrapper