import requests
from bs4 import BeautifulSoup
import mysql.connector as connector

import sys, os.path
config_dir = (
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..'
        )
    )
+ '/collector/')
sys.path.append(config_dir)
import config_info

print(config_info.PARAMS)