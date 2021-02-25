"""logger module create logger, prepares logs directory
"""

import os
import logging
import datetime


def get(name: str, log_level = logging.INFO):
  # Gets or creates a logger
  logger = logging.getLogger(name)
  # set log level
  logger.setLevel(log_level)

  current_date_and_time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
  current_date_and_time_string = str(current_date_and_time)
  extension = ".log"
  if not os.path.exists('logs'):
      os.makedirs('logs')

  file_name =  "logs/" + current_date_and_time_string + extension
  # define file handler and set formatter

  file_handler = logging.FileHandler(file_name)
  formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
  file_handler.setFormatter(formatter)

  # add file handler to logger
  logger.addHandler(file_handler)

  return logger


