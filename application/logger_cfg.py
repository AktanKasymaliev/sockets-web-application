import logging.config
import json

class LoggingConfig:
    
    def __init__(self, app_name: __name__) -> None:
        logging.config.dictConfig(self.get_logger_config())
        self.log = logging.getLogger(app_name)

    def read_json(self) -> dict:
        with open("logging.json", 'r') as f:
            data = json.loads(f.read())
        return data

    def get_logger_config(self) -> dict:
        return self.read_json()
    

