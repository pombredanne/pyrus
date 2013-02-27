from pyrus.mplogging import Logger
from base64 import b64encode, b64decode

logger = Logger('pyrus.util')

def base64encode(plain_str):
	logger.debug('Encoding string: base64')
	return b64encode(plain_str.encode()).decode().replace('\n', '')

def base64decode(encoded_str):
	logger.debug('Decoding string: base64')
	return b64decode(encoded_str.encode()).decode().replace('\n', '')
