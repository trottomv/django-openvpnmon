import os
from setuptools import setup, find_packages
 
README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
  
#Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
  name = 'openvpnmon',
  version = '0.9',
  #packages = ['base', 'mon', 'templates'],
  packages = find_packages(),
  include_package_data = True,
  license = 'GNU AGPL License',
  description = 'OpenVPNmon is a web interface OpenVPN configurator.',
  long_description = README,
  author = 'Luca Ferroni',
  author_email = 'fero@befair.it',
  classifiers =[
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU AGPL', # example license
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
  ]
)
