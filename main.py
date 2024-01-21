import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as Dwait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml
import get_content

config = yaml.safe_load(open("config.yml"))

op = webdriver.ChromeOptions()
ch_driver = webdriver.Chrome(service=ChService(config['drivers']['main']), options=op)
ch_driver.maximize_window()
ch_driver.get(config['website']['category'])
time.sleep(config['website']['delay'])


urls = get_content.get_products_url_from_category(ch_driver)
for url in urls:
    print(url.get_attribute('href'))
print(len(urls))

ch_driver.close()

