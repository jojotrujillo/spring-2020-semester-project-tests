import unittest
import time
from selenium import webdriver
import json


class TestLogin(unittest.TestCase):
    var_dict = {}
    
    @staticmethod
    def test_login(a=None):
        try:
            # with open('account\\selenium_tests\\test_variables.json') as file:  # windows
            with open('account//selenium_tests//test_variables.json') as file:  # linux
                var_dict = json.load(file)
        except IOError:
            print('\n\t**NEED JSON FILE FOR TEST VARIABLES**\n')

        if a is None:
            driver = webdriver.Edge(var_dict['driver_exe'])
        else:
            driver = a

        driver.maximize_window()
        driver.get(var_dict['login_url'])
        time.sleep(2)
        elem = driver.find_element_by_name('username')
        elem.send_keys(var_dict['username'])
        elem = driver.find_element_by_name('password')
        elem.send_keys(var_dict['password'])
        elem = driver.find_element_by_xpath(var_dict['login_button']).click()
        time.sleep(2)

        assert True


if __name__ == '__main__':
    unittest.main()
