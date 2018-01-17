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

        # He notice the page title and header mentioning "Task manager"
        self.assertIn('Task Manager', self.browser.title)

        # He is invited to login to page.
        # He find text box to enter own username
        login_field = self.browser.find_element_by_id("id_username")
        login_field.send_keys("johnsnow")

        #He find text box with hidden text to enter password
        pass_field = self.browser.find_element_by_id("id_password")
        pass_field.send_keys("Johnsnow123")

        #He wants click to login
        login_button = self.browser.find_element_by_name("login")
        login_button.click()

    def test_can_register_to_site(self):
        # John enters our new site
        self.browser.get('http://localhost:8000')

        # He wants click to create new account, so he clicks register button
        register_button = self.browser.find_element_by_name("register")
        register_button.click()

        # So he types his email
        emailbox = self.browser.find_element_by_id("id_email")
        emailbox.send_keys("john@gmail.com")

        # He types his username
        nameBox = self.browser.find_element_by_id("id_username")
        nameBox.send_keys("johnsnow")

        # He types his password
        passwordBox = self.browser.find_element_by_id("id_password1")
        passwordBox.send_keys("Johnsnow123")
        password2Box = self.browser.find_element_by_id("id_password2")
        password2Box.send_keys("Johnsnow123")

        # And finally he click register to create new account
        register_button = self.browser.find_element_by_name("register")
        register_button.click()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
