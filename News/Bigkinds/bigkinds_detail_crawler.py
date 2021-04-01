import maya
import json
import requests
from dateutil.relativedelta import relativedelta
import requests
from bs4 import BeautifulSoup
import mysql.connector as connector

import sys
import os.path
import bigkinds_crawler
config_dir = (
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '../../'
        )
    )
    + '/Attribute/config/')
sys.path.append(config_dir)
import bigkinds


while bigkinds_crawler.response_dic['resultList']:
    bigkinds_crawler.end_date = bigkinds_crawler.end_date + \
        relativedelta(days=-1)
    if(bigkinds_crawler.end_date.year == 2009):
        break
    
    end_date_str = bigkinds_crawler.end_date.strftime("%Y-%m-%d")
    start_date = bigkinds_crawler.end_date + relativedelta(days=-1)
    start_date_str = start_date.strftime('%Y-%m-%d')

    for page_no in range(bigkinds_crawler.total_page):
        bigkinds.PARAMS["startNo"] = page_no + 1
        bigkinds.PARAMS["endDate"] = end_date_str
        bigkinds.PARAMS["startDate"] = start_date_str
        response = requests.post(
            bigkinds.URL,
            headers=bigkinds.HEADERS,
            data=json.dumps(bigkinds_crawler.params)
        )
        # print(response.text)

        detail_response_dic = json.loads(response.text)
        result_list = detail_response_dic["resultList"]
    

def mysql_detail_connector():
    conn = connector.connect(
        user='root',
        passwd='1234',
        host='localhost',
        db='crawl_data_db',
        auth_plugin='mysql_native_password'
    )

    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS `TB_TEST_DETAIL_CRAWLER`")
    cursor.execute("CREATE TABLE `TB_TEST_DETAIL_CRAWLER`(`SEQ` INT NOT NULL, `CONTENTS` TEXT)")

    results = [result for result in zip(detail_response_dic['TITLE'])]
    # print(results)

    i = 1
    for result in results:
        cursor.execute(
            f"INSERT INTO `TB_TEST_DETAIL_CRAWLER` VALUES({i}, \"{result[0]}\")"
        )
        i += 1
    conn.commit()
    conn.close()


if __name__ == "__main__":
    mysql_detail_connector()
