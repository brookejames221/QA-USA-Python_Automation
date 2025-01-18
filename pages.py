import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import helpers
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    supportive_plan = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')
    supportive_text = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    call_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    custom_option = (By.XPATH, '//div[text()= "Custom"]')
    phone_number_button = (By.XPATH, '// *[ @ id = "root"] / div / div[3] / div[3] / div[2] / div[2] / div[1] / div')
    phone_input_field = (By.XPATH, '//*[@id="phone"]')
    next_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    sms_field = (By.XPATH, '//*[@id="code"]')
    payment_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]')
    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div/img')
    card_number = (By.XPATH, '//*[@id="number"]')
    card_code = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input')
    click_off = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]')
    link_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    driver_message_field = (By.XPATH, '//*[@id="comment"]')
    close_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    blankets_and_handkerchiefs = (By.CLASS_NAME, 'switch')
    blankets_and_handkerchiefs_check = (By.CLASS_NAME, 'switch-input')
    add_ice_cream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    counter_value = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    confirm_button = (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    car_search_element = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]')
    order_button = (By.XPATH, '/html/body/div/div/div[3]/div[4]/button')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        from_field = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.from_field))
        from_field.send_keys(from_text)

    def enter_to_location(self, to_text):
        self.driver.find_element(*self.to_field).send_keys(to_text)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.call_taxi_button)
        )
        self.driver.find_element(*self.call_taxi_button).click()

    def set_route(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_call_taxi_button()

    def select_supportive_plan(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.supportive_plan)
        )
        self.driver.find_element(*self.supportive_plan).click()

    def get_supportive_text(self):
        return self.driver.find_element(*self.supportive_text).text

    def click_custom_option(self):
        self.driver.find_element(*self.custom_option).click()

    def enter_phone_number(self, phone_text):
        phone_input_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.phone_input_field)
        )
        phone_input_field.send_keys(phone_text)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_input_field).get_property('value')

    def enter_sms_code(self, sms_text):
        self.driver.find_element(*self.sms_field).send_keys(sms_text)

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.next_button)
        )
        self.driver.find_element(*self.next_button).click()

    def click_phone_number_option(self):
        self.driver.find_element(*self.phone_number_button).click()

    def click_payment_button(self):
        self.driver.find_element(*self.payment_button).click()

    def click_add_card(self):
        self.driver.find_element(*self.add_card_button).click()

    def enter_card_number(self, card_text):
        card_number = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.card_number))
        card_number.send_keys(card_text)

    def enter_card_code(self, code_text):
        self.driver.find_element(*self.card_code).send_keys(code_text)

    def click_out_code(self):
        self.driver.find_element(*self.click_off).click()

    def get_card_number(self):
        return self.driver.find_element(*self.card_number).get_property('value')

    def get_card_code(self):
        return self.driver.find_element(*self.card_code).get_property('value')

    def click_link_button(self):
        self.driver.find_element(*self.link_button).click()

    def enter_driver_message(self, message_text):
        self.driver.find_element(*self.driver_message_field).send_keys(message_text)

    def get_driver_message(self):
        return self.driver.find_element(*self.driver_message_field).get_property('value')

    def order_blankets_and_handkerchiefs(self):
        self.driver.find_element(*self.blankets_and_handkerchiefs).click()

    def is_order_confirmation_displayed(self):
        return self.driver.find_element(*self.blankets_and_handkerchiefs_check).get_property('checked')

    def close_card(self):
        self.driver.find_element(*self.close_card_button).click()

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def click_ice_cream(self):
        self.driver.find_element(*self.add_ice_cream).click()

    def get_counter_value(self):
        return self.driver.find_element(*self.counter_value).text

    def is_car_search_model_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(self.car_search_element)
            )
            return True
        except:
            return False

    def click_confirm(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.confirm_button)
        )
        self.driver.find_element(*self.confirm_button).click()