from crawl.settings import path
from selenium import webdriver


def driver_access(url: str):
    driver = webdriver.Chrome(path)
    driver.get(url)

    return driver
