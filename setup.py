from setuptools import setup, find_packages

setup(name='nmln',
      packages=find_packages(),
      version='0.0.1',
      install_requires=['tensorflow>=2.0',
                        'sortedcontainers',
                        'pyparsing']#And any other dependencies required
)