import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as Dwait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import yaml

config = yaml.safe_load(open("config.yml"))


def get_products_url_from_category(driver):
    """
    Getting all Product urls from the Category
    :param driver: Selenium Driver
    :return: list of URLS
    """
    # ... possibly inject cookie (or local storage value) indicating cookie policy to skip this step
    sel = ".CookiePopup-CTA_isDistinctButtonsStyle > button:nth-child(2)"
    Dwait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, sel)))
    print(f">>>{driver.title}", flush=True)
    allow_selected_cookies_button = driver.find_element(By.CSS_SELECTOR, sel)
    allow_selected_cookies_button.click()
    scroll_to_end(driver)
    time.sleep(config['website']['delay'])

    load_all = driver.find_element(By.XPATH, config['website']['get_all_button'])
    load_all.click()
    time.sleep(config['website']['delay'])

    scroll_to_end(driver)

    all_product_url = driver.find_elements(By.CLASS_NAME, 'ProductCard-Link')
    return all_product_url


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
