from distutils.core import setup
from setuptools import find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='code_chess',
    version='0.0.2',
    packages=['test', 'chess'],
    url='https://github.com/churq/code_chess',
    license='licence',
    author='Rachel Chu',
    author_email='churq@hotmail.com',
    description='This simple project is an example repo for Python projects to demonstrate the best practices.',
    long_description=readme
)
