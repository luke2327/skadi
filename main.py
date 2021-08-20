from selenium import webdriver

path = "C:/chromedriver/chromedriver.exe"
url = "https://poro.gg/"

driver = webdriver.Chrome(path)

driver.get(url)

elem = driver.find_element_by_tag_name("input")

elem.clear()

elem.send_keys("Selenium")

btn = driver.find_element_by_xpath("//button[@type='submit']")

btn.click()
