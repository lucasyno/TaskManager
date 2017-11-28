from selenium import webdriver
import unittest


class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_login_to_site(self):
        # John has heard about our new site called Task Manager. He goes to
        # check out its homepage.
        self.browser.get('http://localhost:8000')

        # He notice the page title and header mentioning "task manager"
        self.assertIn('Task Manager', self.browser.title)

        # He is invited to login to page or to create account.
        self.fail("breakpoint")


if __name__ == '__main__':
    unittest.main(warnings='ignore')