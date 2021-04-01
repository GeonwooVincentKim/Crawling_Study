import maya
import json
from dateutil.relativedelta import relativedelta
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

end_date = maya.now().datetime(to_timezone="Asia/Seoul") + relativedelta(days=1)
params = config_info.PARAMS
params["endDate"] = (end_date + relativedelta(days=-1)).strftime('%Y-%m-%d')
params["startDate"] = (end_date + relativedelta(days=-2)).strftime('%Y-%m-%d')
response = requests.post(
    config_info.URL, 
    data=json.dumps(params), 
    headers=config_info.HEADERS
)

print(response.status_code)
json_result = response.json()
print(json_result)

response_dic = json.loads(response.text)
total_count = response_dic["totalCount"]
total_page = total_count // 10 if total_count % 10 == 0 else total_count // 10 + 1
print(total_page)

conn = connector.connect(
    user='root',
    passwd='1234',
    host='localhost',
    db='crawl_data_db',
    auth_plugin='mysql_native_password'
)

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS `TB_TEST_CRAWLER`")
cursor.execute("CREATE TABLE `TB_TEST_CRAWLER`(`SEQ` INT NOT NULL, `CONTENTS` TEXT)")

results = [result for result in zip(response_dic['getCategoryCodeList'])]
print(results)

i = 1
for result in results:
    cursor.execute(
        f"INSERT INTO `TB_TEST_CRAWLER` VALUES({i}, \"{result[0]}\")"
    )
    i += 1
conn.commit()
conn.close()