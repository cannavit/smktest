from setuptools import setup, find_packages
from distutils.core import setup

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()


setup(
  name = 'smktest',
  packages = ['smktest'], # this must be the same as the name above
  version = '0.1',
  description = 'This package offers a series of tests to create the correct Smoke Test of an application before uploading changes to production.',
  author = 'Cecilio Cannavacciuolo Díaz',
  author_email = 'cecilio.cannav@gmail.com',
  url = 'https://github.com/{user_name}/{repo}', # use the URL to the github repo
  download_url = 'https://github.com/{user_name}/{repo}/tarball/0.1',
  keywords = ['smoketest', 'testing', 'python', 'smart',],
  classifiers = [],
)

install_requires = [
  #  'elasticsearch>=6.0.0,<7.0.0',
    'subprocess',
    'requests',
    'json',
    'pytest',
    'pyhttptest',
]
