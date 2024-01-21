import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChService
import yaml
import get_content


config = yaml.safe_load(open("config.yml"))
category_file_name = config['results']['categories_file']

op = webdriver.ChromeOptions()
ch_driver = webdriver.Chrome(service=ChService(config['drivers']['main']), options=op)
ch_driver.maximize_window()


# get category's from Homepage
ch_driver.get(config['website']['homepage'])
time.sleep(config['website']['delay'])

get_content.set_cookies(ch_driver)

# need to use def get_categories(driver) but ths function not finished
products_urls = get_content.get_products_url_from_category(ch_driver, "https://sportland.lt/vyrai/avalyne/batai")
products_urls_list = []
for url in products_urls:
    products_urls_list.append(url.get_attribute('href') + '\n')

get_content.write_to_file(config['results']['product_file'], products_urls_list)


# Open the file in read mode
with open(config['results']['product_file'], 'r') as file:
    # Read the lines from the file into a list
    product_list_urls = file.read().splitlines()

for row in product_list_urls:
    image = get_content.get_product_image(ch_driver, row)
    get_content.write_to_file(config['results']['image_file'], [image])

ch_driver.close()

