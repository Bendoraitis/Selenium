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


# get category's from Homepage
print(config['website']['homepage'])
ch_driver.get(config['website']['homepage'])
time.sleep(config['website']['delay'])

get_content.set_cookies(ch_driver)

# all_categories = ch_driver.find_elements(By.CLASS_NAME, 'MenuOverlay-Link')
all_categories = ch_driver.find_elements(By.CLASS_NAME, 'CategoryMenu-Item')
for url in all_categories:
    print(url.get_attribute('href'))
print(len(all_categories))
#
#
# urls = get_content.get_products_url_from_category(ch_driver, "https://sportland.lt/moterys/avalyne/laisvalaikis")
#
#
#
# for url in urls:
#     print(url.get_attribute('href'))
# print(len(urls))

ch_driver.close()

