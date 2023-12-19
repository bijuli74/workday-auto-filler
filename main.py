import os
import time
import argparse
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    options = Options()
    options.add_experimental_option("detach", True)
    # options.add_extension('CJPALHDLNBPAFIAMEJDNHCPHJBKEIAGM_1_54_0_0.crx')
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    data = {}
    with open('data.yaml') as file:
        try:
            data = yaml.safe_load(file)
            # for key, value in data.items():
            #     print(key, ":", value)
        except yaml.YAMLError as exception:
            print(exception)

    url = data['url']
    driver.get(url)
    time.sleep(60)

# Scroll to the bottom of the page
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # Wait for the page to load completely
#     wait = WebDriverWait(driver, 10)
#     wait.until(lambda driver: driver.execute_script(
#         "return document.readyState") == "complete")

    # driver.execute_script("document.body.style.zoom = '25%'")

    prev_worker = data['prev-worked-here']
    if prev_worker == "yes":
        qry_prev_worker = "//*[@data-automation-id = 'previousWorker']//input[@id='1']"
    else:
        qry_prev_worker = "//*[@data-automation-id = 'previousWorker']//input[@id='2']"
    prev_worker_radio_ele = driver.find_element("xpath", qry_prev_worker)
    prev_worker_radio_ele.click()

    first_name = data['firstname']
    qry_firstname = "//*[@data-automation-id = 'legalNameSection_firstName']"
    qry_firstname_ele = driver.find_element("xpath", qry_firstname)
    qry_firstname_ele.send_keys(first_name)

    last_name = data['lastname']
    qry_lastname = "//*[@data-automation-id = 'legalNameSection_lastName']"
    qry_lastname_ele = driver.find_element("xpath", qry_lastname)
    qry_lastname_ele.send_keys(last_name)

    address1 = data['address1']
    qry_address1 = "//*[@data-automation-id = 'addressSection_addressLine1']"
    address1_ele = driver.find_element("xpath", qry_address1)
    address1_ele.send_keys(address1)

    city = data['city']
    query_city = "//*[@data-automation-id = 'addressSection_city']"
    city_ele = driver.find_element("xpath", query_city)
    city_ele.send_keys(city)

    pincode = data['pincode']
    qry_pincode = "//*[@data-automation-id = 'addressSection_postalCode']"
    pincode_ele = driver.find_element("xpath", qry_pincode)
    pincode_ele.send_keys(pincode)

    time.sleep(10)

    state_name = data['state']
    qry_state_ddl = "//button[@data-automation-id='addressSection_countryRegion']"
    dropdown_button_state = driver.find_element("xpath", qry_state_ddl)
    hover = ActionChains(driver).move_to_element(dropdown_button_state)
    hover.click().perform()
    wait = WebDriverWait(driver, 200)
    desired_option_state = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//ul/li/div[contains(text(), state_name)]")))
    desired_option_state.click()

    time.sleep(5)

    ph_no = data['phone-no']
    query_ph_no = "//*[@data-automation-id = 'phone-number']"
    ph_no_ele = driver.find_element("xpath", query_ph_no)
    ph_no_ele.send_keys(ph_no)

    phone_type = data['phone-device-type']
    qry_phone_ddl = "//button[@data-automation-id='phone-device-type']"
    dropdown_button = driver.find_element("xpath", qry_phone_ddl)
    hover = ActionChains(driver).move_to_element(dropdown_button)
    hover.click().perform()
    wait = WebDriverWait(driver, 20)
    desired_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//ul/li/div[contains(text(), 'Cell')]")))
    desired_option.click()

    # Next button
    next_button = "//*[@data-automation-id = 'bottom-navigation-next-button']"
    next_button_ele = driver.find_element("xpath", next_button)
    next_button_ele.clid()

    print("ALL FINISHED!!!")
    # driver.quit()


if __name__ == '__main__':
    main()

