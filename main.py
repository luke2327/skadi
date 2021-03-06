from selenium import webdriver
from flask import jsonify
from db.query import execute
from crawl.default import driver_access

import lib.champions_dict as champions_info


def get_champions_info(champions_name: str):
    url = "https://poro.gg/"

    driver = driver_access(url)

    elem = driver.find_element_by_tag_name("input")
    elem.clear()
    elem.send_keys(champions_name)

    btn = driver.find_element_by_xpath("//button[@type='submit']")
    btn.click()


def get_champions_info_by_dict(champions_name: str):
    if champions_info.champions_info_match_kr[champions_name]:
        champions_original_name = \
            champions_info.champions_info_match_kr[champions_name]

        champions_desc = \
            champions_info.champions_story_kr[champions_original_name]

        return jsonify({'champions_desc': champions_desc})


def query_test(champions_name: str):
    champions_original_name = \
        champions_info.champions_info_match_kr[champions_name]

    query = f'INSERT INTO temp(testval) VALUES(`{champions_original_name}`)'

    execute(query=query)
