import unittest
from selenium import webdriver



class JiraLoginTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()


    def login(self, login, pw):
        self.browser.get("https://jira.wsb.wroclaw.pl")
        login_input = self.browser.find_element_by_id("login-form-username")
        login_input.send_keys(login)
        passwrd = self.browser.find_element_by_id("login-form-password")
        passwrd.send_keys(pw)
        self.browser.find_element_by_id("login").click()
        create_button = self.browser.find_element_by_id("create_link").is_displayed()



    def test_login_to_jira(self,):
        self.login("przemo", "takiegouseratuniema")

if __name__ == "__main__":
    unittest.main()