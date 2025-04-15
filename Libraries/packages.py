# packages, or third party libraries

# PyPI, pypi.org

# pip
# pip is a program that installs Python packages


# pip install cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])


# APIs, Application Programming Interface
# API is a set of functions and procedures that allow the creation of applications

# requests library in python allows you to make internet, HTTP, requests as if you were a web browser
# pypi.org/project/requests/
# pip install requests

# import requests

import requests
import sys


