import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import json


class TestRecoverPassword(unittest.TestCase):
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
        cls.driver.maximize_window()
        cls.driver.get(cls.var_dict['login_url'])
        time.sleep(2)

    # @unittest.skip('already tested')
    def test_recover_password(self):
        self.driver.find_element_by_xpath(self.var_dict['recover_password_link']).click()
        time.sleep(2)
        elem = self.driver.find_element_by_name('email')
        elem.send_keys(self.var_dict['email'])
        self.driver.find_element_by_xpath(self.var_dict['send_recovery_email_button']).click()
        link = input('\n**Enter password recovery link: ')
        self.driver.get(link)
        time.sleep(2)
        elem = self.driver.find_element_by_name('new_password1')
        elem.send_keys(self.var_dict['new_password'])
        elem = self.driver.find_element_by_name('new_password2')
        elem.send_keys(self.var_dict['new_password'])
        self.driver.find_element_by_xpath(self.var_dict['change_recovered_password_button']).click()
        time.sleep(2)

        assert self.driver.find_element_by_xpath(self.var_dict['password_set_xpath']).text == self.var_dict['password_set_message']

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()