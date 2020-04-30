import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import json
from . import test_login as login


class TestEditProfile(unittest.TestCase):
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
        cls.driver.find_element_by_xpath(cls.var_dict['edit_profile_button']).click()
        time.sleep(2)

    # @unittest.skip('already tested')
    def test_edit_profile(self):
        elem = self.driver.find_element_by_name('last_name')
        elem.send_keys('User')
        elem = self.driver.find_element_by_name('date_of_birth')
        elem.send_keys('1970-01-01')
        elem = self.driver.find_element_by_name('photo')
        elem.send_keys(self.var_dict['profile_picture_local'])
        self.driver.find_element_by_xpath(self.var_dict['save_changes_button']).click()
        time.sleep(2)

        assert self.driver.find_element_by_class_name('success')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
