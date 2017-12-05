from selenium import webdriver
import unittest


class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_login_to_site(self):
        # John has heard about our new site called Task Manager. He goes to
        # check out its homepage.
        self.browser.get('http://localhost:8000')

        # He notice the page title and header mentioning "task manager"
        self.assertIn('Task Manager', self.browser.title)

        # He is invited to login to page.
        # He find text box to enter own username
        login_field = self.browser.find_element_by_id("username")
        login_field.send_keys("Admin")

        #He find text box with hidden text to enter password
        pass_field = self.browser.find_element_by_id("password")
        pass_field.send_keys("Admin")

        #He wants click to login
        login_button = self.browser.find_element_by_name("Login")
        login_button.click()

        # # He wants click to create new acc
        # register_button = self.browser.find_element_by_name("New_Member")
        # register_button.click()








if __name__ == '__main__':
    unittest.main(warnings='ignore')
