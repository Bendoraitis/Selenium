import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChService
from selenium.webdriver.firefox.service import Service as FFService
import yaml
config = yaml.safe_load(open("config.yml"))

print(config['website']['category'])

op = webdriver.ChromeOptions()
ch_driver = webdriver.Chrome(service=ChService(config['drivers']['main']), options=op)
ch_driver.maximize_window()
ch_driver.get(config['website']['category'])
time.sleep(5)
print(ch_driver.title)

ch_driver.close()

print(dir())
