import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import json
from . import test_login as login


class TestPostImage(unittest.TestCase):
    var_dict = {}

    @classmethod
    def setUpClass(cls):
        try:
            # with open('account\\selenium_tests\\test_variables.json') as file:  # windows
            with open('account//selenium_tests//test_variables.json') as file:  # linux
                cls.var_dict = json.load(file)
        except IOError:
            print('\n\t**NEED JSON FILE FOR TEST VARIABLES**\n')

        cls.driver = webdriver.Edge(cls.var_dict['driver_exe'])
        login.TestLogin().test_login(cls.driver)
        time.sleep(10)

    # @unittest.skip('already tested')
    def test_post_image(self):
        self.driver.get('https://www.circuitcity.com/#')
        elem = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'bookmarklet')))
        time.sleep(2)
        self.driver.find_element_by_xpath(self.var_dict['first_image_to_post']).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        elem = self.driver.find_element_by_id('id_title')
        self.driver.execute_script('arguments[0].setAttribute("value","Computer Stuff")', elem)
        elem = self.driver.find_element_by_id('id_description')
        elem.send_keys('This computer stuff looks nice')
        self.driver.find_element_by_xpath(self.var_dict['bookmark_it_button']).click()
        time.sleep(2)
        
        assert self.driver.find_element_by_class_name('success')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
