"""
Module to run Selenium tests
"""
import unittest
from account.selenium_tests import test_register, test_recover_password, test_login, test_change_password, test_edit_profile, test_follow_user, test_like_image, test_post_image


REGISTER = unittest.TestLoader().loadTestsFromTestCase(test_register.TestRegister)
RECOVER_PASSWORD = unittest.TestLoader().loadTestsFromTestCase(test_recover_password.TestRecoverPassword)
LOGIN = unittest.TestLoader().loadTestsFromTestCase(test_login.TestLogin)
CHANGE_PASSWORD = unittest.TestLoader().loadTestsFromTestCase(test_change_password.TestChangePassword)
EDIT_PROFILE = unittest.TestLoader().loadTestsFromTestCase(test_edit_profile.TestEditProfile)
FOLLOW_USER = unittest.TestLoader().loadTestsFromTestCase(test_follow_user.TestFollowUser)
LIKE_IMAGE = unittest.TestLoader().loadTestsFromTestCase(test_like_image.TestLikeImage)
POST_IMAGE = unittest.TestLoader().loadTestsFromTestCase(test_post_image.TestPostImage)

ACCOUNT_TEST_SUITE = unittest.TestSuite([REGISTER, RECOVER_PASSWORD, LOGIN, CHANGE_PASSWORD, EDIT_PROFILE, FOLLOW_USER, LIKE_IMAGE, POST_IMAGE]) # add TestCase classes to TestSuite

unittest.TextTestRunner(verbosity=2).run(ACCOUNT_TEST_SUITE)
