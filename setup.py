"""Ran to set up the project and install the required
third-party dependencies through PIP."""

from setuptools import setup
from pip.req import parse_requirements

REQUIREMENTS = [
    str(ir.req) for ir in parse_requirements('requirements.txt', session=False)
]

setup(
    name='ctpcj',
    version='1.0.0',
    author='Swen Kooij',
    author_email='photonios@outlook.com',
    description='CTPCJ back-end server.',
    install_requires=REQUIREMENTS
)
