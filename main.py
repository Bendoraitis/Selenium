import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChService
from selenium.webdriver.firefox.service import Service as FFService


op = webdriver.ChromeOptions()
# get drivers from here: https://googlechromelabs.github.io/chrome-for-testing/#stable
ch_driver = webdriver.Chrome(service=ChService('drivers/chromedriver_v120.0.6099.109'), options=op)
ch_driver.maximize_window()
ch_driver.get("https://sportland.lt/")
time.sleep(5)
print(ch_driver.title)
input()
ch_driver.close()


print(dir())