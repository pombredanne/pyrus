#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
	name='pyrus',
	version='0.0.1',
	description='Python helper module.',
	long_description='',
	author='Arun Babu Neelicattu',
	url="https://github.com/abn/pyrus",
	download_url="https://github.com/abn/pyrus",

	install_requires=[],

	# license="",

	packages=find_packages('src'),
	package_dir={'': 'src'},
	include_package_data=True,

	# test_suite="",

	classifiers=[
		'Intended Audience :: Developers',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
)
