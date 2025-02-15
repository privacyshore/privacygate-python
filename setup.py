"""Setup script for PrivacyGate API client.
Also installs included versions of third party libraries, if those libraries
are not already installed.
"""
import os

from setuptools import setup

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

version_contents = {}
with open(os.path.join(ROOT_DIR, 'privacygate', 'version.py')) as f:
    exec(f.read(), version_contents)

with open(os.path.join(ROOT_DIR, 'README.md')) as f:
    long_description = f.read()

packages = [
    'privacygate',
    'privacygate.api_resources',
    'privacygate.api_resources.base',
]

install_requires = [
    'requests>=2.14.0,<3',
    'six>=1.9,<2',
]

tests_require = [
    'coverage>=4,<5',
    'unittest2>=0.8.0,<1',
    'mock>=2.0.0,<3',
]

setup(
    name='privacygate',
    version=version_contents['VERSION'],
    packages=packages,
    include_package_data=True,
    license='Apache 2.0',
    description='PrivacyGate API client library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/privacyshore/privacygate-python',
    keywords=['api', 'privacygate', 'client', 'bitcoin', 'payment gateway'],
    install_requires=install_requires,
    extras_require={
        'dev': ['nose>=1.3.4,<2', 'flake8>=3.5.0,<4'] + tests_require,
    },
    tests_require=tests_require,
    author='PrivacyGate',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
