import re
import os
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


class Logger():
	def __init__(self, directory):
		log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
		log_directory = self.create_log_folder(directory)
		logFile = os.path.join(directory, "log")
		my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=10*1024*1024, 
		                                 backupCount=10, encoding=None, delay=0)
		my_handler.setFormatter(log_formatter)
		my_handler.setLevel(logging.INFO)
		self.log = logging.getLogger('root')
		self.log.setLevel(logging.INFO)
		self.log.addHandler(my_handler)

	def debug(self, message):
		self.log.error(message)	

	def info(self, message):
		self.log.info(message)

	def warning(self, message):
		self.log.warning(message)

	def error(self, message):
		self.log.error(message)

	def critical(self, message):
		self.log.critical(message)

	def create_log_folder(self, directory):
		if not os.path.exists(directory):
			os.mkdir(directory)