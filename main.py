from selenium import webdriver
from lib.champions_dict import champions_info_match_kr

path = "C:/chromedriver/chromedriver.exe"


def get_champions_info(champions_name):
    url = "https://poro.gg/"

    driver = driver_access(url)

    elem = driver.find_element_by_tag_name("input")
    elem.clear()
    elem.send_keys(champions_name)

    btn = driver.find_element_by_xpath("//button[@type='submit']")
    btn.click()


def get_champions_info_by_dict(champions_name):
    if champions_info_match_kr[champions_name]:
        url = champions_info_match_kr[champions_name]

        driver_access(url)

        return url


def driver_access(url):
    driver = webdriver.Chrome(path)
    driver.get(url)

    return driver
