import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as Dwait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import yaml
import os

config = yaml.safe_load(open("config.yml"))


def get_products_url_from_category(driver, url):
    """
    Getting all Product urls from the Category
    :param driver: Selenium Driver
    :return: list of URLS
    """

    driver.get(url)
    time.sleep(config['website']['delay'])

    load_all = driver.find_element(By.XPATH, config['website']['get_all_button'])
    load_all.click()
    time.sleep(config['website']['delay'])

    scroll_to_end(driver)

    all_product_url = driver.find_elements(By.CLASS_NAME, 'ProductCard-Link')
    return all_product_url


def get_product_image(driver, url):
    """
    Getting all Product urls from the Category
    :param driver: Selenium Driver
    :return: list of URLS
    """

    driver.get(url)
    time.sleep(config['website']['delay'])

    load_all = driver.find_element(By.XPATH, '//*[@id="root"]/main/section/div/div/div[3]/div/div/div/div[1]/div/button/div')
    load_all.click()
    time.sleep(config['website']['delay'])

    main_image = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div[1]/div[1]/div/button/div/img')

    img = main_image.get_attribute('src')
    return img



def scroll_to_end(driver):
    """
    Scrolling webpage to end
    :param driver: Selenium Driver
    :return:
    """
    # Find any element at the top of the page
    top_element = driver.find_element(By.TAG_NAME, 'body')

    # Move to the top element to make sure the actions are applied to it
    ActionChains(driver).move_to_element(top_element).perform()

    # Imitate mouse wheel scrolling to the end
    for _ in range(10):  # Adjust the number of iterations as needed
        ActionChains(driver).send_keys(Keys.END).perform()
        time.sleep(1)  # Adjust sleep duration if needed


def set_cookies(driver):
    # inject cookie
    sel = ".CookiePopup-CTA_isDistinctButtonsStyle > button:nth-child(2)"
    Dwait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, sel)))
    allow_selected_cookies_button = driver.find_element(By.CSS_SELECTOR, sel)
    allow_selected_cookies_button.click()
    time.sleep(config['website']['delay'])


# not finished for categories getting....
def get_categories(driver):
    all_categories = driver.find_elements(By.CLASS_NAME, 'MenuOverlay-Link')

    # Check if the file already exists
    file_exists = os.path.isfile(config['results']['categories_file'])

    category_urls = []
    for row in all_categories:
        category_urls.append(row.get_attribute('href') + '\n')

        with open(config['results']['categories_file'], 'a') as file:
            file.writelines(row.get_attribute('href') + '\n')

        remove_duplicates_from_file(config['results']['categories_file'])


def write_to_file(file_name, data_list):
    file_exists = os.path.isfile(file_name)
    # Open the file in write mode
    with open(file_name, 'a') as file:
        # Write each element to a new line
        for item in data_list:
            file.write(item + '\n')
    remove_duplicates_from_file(file_name)


def remove_duplicates_from_file(file_name):
    # remove duplicates
    uniq_lines = set(open(file_name).readlines())
    open(file_name, 'w').writelines(uniq_lines)
