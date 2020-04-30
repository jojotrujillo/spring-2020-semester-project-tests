"""
Selenium test module for 'change password' feature
"""
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import json
from . import test_login as login


class TestChangePassword(unittest.TestCase):
    """
    TestCase class for 'change password' feature
    """
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
        cls.driver.find_element_by_xpath(cls.var_dict['change_password_link']).click()
        time.sleep(2)

    @unittest.skip('already tested')
    def test_invalid_new(self):
        """
        Test change password feature with an invalid new password
        :return: returns nothing
        """
        elem = self.driver.find_element_by_name('old_password')
        elem.send_keys(self.var_dict['password'])
        elem = self.driver.find_element_by_name('new_password1')
        elem.send_keys('thetest')
        elem = self.driver.find_element_by_name('new_password2')
        elem.send_keys('thetest')
        self.driver.find_element_by_xpath(self.var_dict['submit_chg_pwd_button']).click()
        time.sleep(5)

        assert self.driver.find_element_by_xpath(self.var_dict['invalid_new_message_xpath']).text == self.var_dict['invalid_new_message']

    @unittest.skip('already tested')
    def test_invalid_old(self):
        """
        Test change password feature with invalid old password
        :return: returns nothing
        """
        elem = self.driver.find_element_by_name('old_password')
        elem.send_keys('maverick1c')
        elem = self.driver.find_element_by_name('new_password1')
        elem.send_keys('thetest247')
        elem = self.driver.find_element_by_name('new_password2')
        elem.send_keys('thetest247')
        self.driver.find_element_by_xpath(self.var_dict['submit_chg_pwd_button']).click()
        time.sleep(5)

        assert self.driver.find_element_by_xpath(self.var_dict['invalid_old_message_xpath']).text == self.var_dict['invalid_old_message']

    @unittest.skip('already tested')
    def test_mismatched(self):
        """
        Test change password feature with mismatched new passwords
        :return: returns nothing
        """
        elem = self.driver.find_element_by_name('old_password')
        elem.send_keys(self.var_dict['password'])
        elem = self.driver.find_element_by_name('new_password1')
        elem.send_keys('thetest247')
        elem = self.driver.find_element_by_name('new_password2')
        elem.send_keys('thetest365')
        self.driver.find_element_by_xpath(self.var_dict['submit_chg_pwd_button']).click()
        time.sleep(5)

        assert self.driver.find_element_by_xpath(self.var_dict['mismatched_message_xpath']).text == self.var_dict['mismatched_message']

    #@unittest.skip('already tested')
    def test_valid_new(self):
        """
        Test change password feature with a valid new password
        :return: returns nothing
        """        
        elem = self.driver.find_element_by_name('old_password')
        elem.send_keys(self.var_dict['password'])
        elem = self.driver.find_element_by_name('new_password1')
        elem.send_keys(self.var_dict['new_password'])
        elem = self.driver.find_element_by_name('new_password2')
        elem.send_keys(self.var_dict['new_password'])
        self.driver.find_element_by_xpath(self.var_dict['change_password_again_button']).click()
        time.sleep(2)

        assert self.driver.find_element_by_xpath(self.var_dict['valid_new_message_xpath']).text == self.var_dict['valid_new_message']

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
