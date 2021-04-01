import maya
import json
from dateutil.relativedelta import relativedelta
import requests
from bs4 import BeautifulSoup
import mysql.connector as connector

import sys
import os.path
config_dir = (
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '../../'
        )
    )
    + '/Bigkinds/')
sys.path.append(config_dir)
import bigkinds_crawler


conn = connector.connect(
    user='root',
    passwd='1234',
    host='localhost',
    db='crawl_data_db',
    auth_plugin='mysql_native_password'
)
