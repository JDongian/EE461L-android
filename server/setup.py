from setuptools import setup, find_packages
import sys

if sys.version_info <= (3, 0):
    print("ERROR: server requires Python 3.0 or later "
          , file=sys.stderr)
    sys.exit(1)

setup(
    name="server",
    version="0.01",
    description="EE461L REST API and web server",
    author="Joshua Dong",
    author_email="jdong42@gmail.com",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    install_requires=[
        "flask >= 0.10.1",
        "flask-wtf",
        "flask-login",
        "flask-sqlalchemy",
    ],
    packages=find_packages(),
    package_dir={'app': 'app'},
)
