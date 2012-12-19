from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-datahubsuomi',
	version=version,
	description="Customizations for fi.thedatahub.org.",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Jaakko Louhio',
	author_email='jaakko.louhio@floapps.com',
	url='http://fi.thedatahub.org',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.datahubsuomi'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
	[ckan.plugins]
	datahubsuomi=ckanext.datahubsuomi.plugin:DatahubSuomi
	""",
)
