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
import csv
import os

config = yaml.safe_load(open("config.yml"))
category_file_name = config['results']['categories_file']

op = webdriver.ChromeOptions()
ch_driver = webdriver.Chrome(service=ChService(config['drivers']['main']), options=op)
ch_driver.maximize_window()


# get category's from Homepage
print(config['website']['homepage'])
ch_driver.get(config['website']['homepage'])
time.sleep(config['website']['delay'])

get_content.set_cookies(ch_driver)


products_urls = get_content.get_products_url_from_category(ch_driver, "https://sportland.lt/vyrai/avalyne/batai")
products_urls_list = []
for url in products_urls:
    products_urls_list.append(url.get_attribute('href') + '\n')

get_content.write_to_file(config['results']['product_file'], products_urls_list)

ch_driver


ch_driver.close()

