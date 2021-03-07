"""
config module reads configuration 
"""
import yaml

import themagen.log


def read(config_filename = 'config.yml'):
    logger = themagen.log.get(__name__)
    try:
        with open(config_filename, 'r') as ymlfile:
            cfg = yaml.load(ymlfile, yaml.FullLoader) 
        return cfg  
    except OSError as e:
        logger.error(f"error while open/read file {config_filename} details {str(e)}")
        raise e