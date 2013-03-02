from http.cookiejar import CookieJar
from urllib.request import build_opener, urlopen, HTTPCookieProcessor
from urllib.error import HTTPError
from urllib.parse import urlencode
from copy import deepcopy
from pyrus.util import base64encode, base64decode

class CookiedOpener:
	def __init__(self, cj=CookieJar()):
		self.cj = cj
		self.opener = build_opener(HTTPCookieProcessor(cj))
		self.addheaders = self.opener.addheaders

	def open(self, url, data=None, timeout=None):
		response = self.opener.open(url, data, timeout)
		return response

	def set_in_cookie(self, key):
		return key in [ c.name for c in self.cj ]

	def add_handler(self, handler):
		return self.opener.add_handler(handler)

	def error(self, proto, *args):
		return self.opener.error(proto, *args)

	def copy(self):
		return CookiedOpener(deepcopy(self.cj))

def encode_base64_auth(username='', password=''):
	"""
	Return a base64 encoded username:password string
	"""
	creds = '%s:%s' % (username, password)
	base64string = base64encode(creds)
	return base64string

def encode_url_data(contents=[]):
	"""Given a list of (key,value), this method returns a urlencoded data
	"""
	data = {}
	for k, v in contents:
		data[k] = v
	data = urlencode(data)
	binary_data = data.encode('utf-8')
	return binary_data

def open_url(url, opener=build_opener(), data=None):
	"""Wrapper function for urllib.request to return a response.
	"""
	response = opener.open(url, data)
	return response

def test_url(url):
	"""Checks if a url resource is available. Returns True if response status
	is in (200, 301, 302)."""
	try:
		response = urlopen(url, timeout=1)
		return response.status in (200, 301, 302)
	except:
		return False

def _response(arg):
	if isinstance(arg, str):
		return open_url(arg)
	return arg

def get_header_value(response, key):
	"""Get the value for a header attribute
	"""
	info = response.info()
	if key in info:
		return info[key]
	return None

def test_header_value(response, key, value):
	"""Test if the value for a header attribute matches a given value.
	"""
	actual_value = get_header_value(response, key)
	if actual_value is not None:
		return value == actual_value
	return False

def is_chunked(response):
	"""Check if the transfer encoding is chunked
	"""
	return test_header_value(response, 'Transfer-Encoding', 'chunked')

def is_range_accepted(response):
	"""
	Check if multiple connections are allowed
	"""
	return test_header_value(response, 'Accept-Ranges', 'bytes')
