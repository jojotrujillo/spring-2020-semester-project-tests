import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import json
from . import test_login as login


class TestFollowUser(unittest.TestCase):
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
        cls.driver.find_element_by_xpath(cls.var_dict['people_link']).click()
        time.sleep(2)

    # @unittest.skip('already tested')
    def test_follow_user(self):
        self.driver.find_element_by_xpath(self.var_dict['fifth_user']).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.var_dict['follow_button']).click()
        time.sleep(2)
        
        assert self.driver.find_element_by_xpath(self.var_dict['user_follower_count_xpath']).text == '2'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()