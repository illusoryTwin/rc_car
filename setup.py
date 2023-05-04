from setuptools import setup

setup(
    name='car',
    version='0.1',
    packages=['car'],
    description='Module to test robotic car',
    install_requires=[line for line in open('requirements.txt').readlines()]
)
