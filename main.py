#Import Files
import time
from selenium import webdriver
import data
import helpers
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

#Testing Functions
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)

        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_call_taxi_button()

        assert urban_routes_page.get_from() == data.ADDRESS_FROM
        assert urban_routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.select_supportive_plan()

        actual_value = urban_routes_page.get_supportive_text()
        expected_value = "Supportive"
        assert actual_value == expected_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.click_phone_number_option()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        sms_code=helpers.retrieve_phone_code(self.driver)
        urban_routes_page.enter_sms_code(sms_code)
        assert urban_routes_page.get_phone_number() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.click_payment_button()
        urban_routes_page.click_add_card()
        urban_routes_page.enter_card_number(data.CARD_NUMBER)
        urban_routes_page.enter_card_code(data.CARD_CODE)
        urban_routes_page.click_out_code()
        urban_routes_page.click_link_button()

        assert urban_routes_page.get_card_number() == data.CARD_NUMBER
        assert urban_routes_page.get_card_code() == data.CARD_CODE

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.enter_driver_message(data.MESSAGE_FOR_DRIVER)

        assert urban_routes_page.get_driver_message() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.enter_driver_message(data.MESSAGE_FOR_DRIVER)
        urban_routes_page.click_payment_button()
        urban_routes_page.click_add_card()
        urban_routes_page.enter_card_number(data.CARD_NUMBER)
        urban_routes_page.enter_card_code(data.CARD_CODE)
        urban_routes_page.click_out_code()
        urban_routes_page.click_link_button()
        urban_routes_page.close_card()
        urban_routes_page.order_blankets_and_handkerchiefs()

        assert urban_routes_page.is_order_confirmation_displayed(), "Order confirmation for blankets and handkerchiefs was not displayed."

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.enter_driver_message(data.MESSAGE_FOR_DRIVER)
        urban_routes_page.click_payment_button()
        urban_routes_page.click_add_card()
        urban_routes_page.enter_card_number(data.CARD_NUMBER)
        urban_routes_page.enter_card_code(data.CARD_CODE)
        urban_routes_page.click_out_code()
        urban_routes_page.click_link_button()
        urban_routes_page.close_card()
        number_of_ice_creams = 2

        for i in range(number_of_ice_creams):
            urban_routes_page.click_ice_cream()

        assert int(urban_routes_page.get_counter_value()) == 2

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_custom_option()
        urban_routes_page.click_call_taxi_button()
        urban_routes_page.select_supportive_plan()
        urban_routes_page.click_phone_number_option()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        sms_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.enter_sms_code(sms_code)
        urban_routes_page.click_confirm()
        urban_routes_page.click_payment_button()
        urban_routes_page.click_add_card()
        urban_routes_page.enter_card_number(data.CARD_NUMBER)
        urban_routes_page.enter_card_code(data.CARD_CODE)
        urban_routes_page.click_out_code()
        urban_routes_page.click_link_button()
        urban_routes_page.close_card()
        urban_routes_page.enter_driver_message(data.MESSAGE_FOR_DRIVER)
        urban_routes_page.order_blankets_and_handkerchiefs()

        number_of_ice_creams = 2
        for i in range(number_of_ice_creams):
            urban_routes_page.click_ice_cream()

        urban_routes_page.click_order_button()

        assert urban_routes_page.is_car_search_model_displayed(), "The car search model did not appear as expected"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()