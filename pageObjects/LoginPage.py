from selenium import webdriver

class LoginPage:
    login_id="Email"
    login_psw="Password"
    login_in_css="button[type='submit']"
    login_out_xpath="//a[@href='/logout']"

    def __init__(self,driver):
        self.driver=driver

    def userName(self,username):
        self.driver.find_element_by_id(self.login_id).clear()
        self.driver.find_element_by_id(self.login_id).send_keys(username)
    def userpsw(self,password):
        self.driver.find_element_by_id(self.login_psw).clear()
        self.driver.find_element_by_id(self.login_psw).send_keys(password)
    def clicklogin(self):
        self.driver.find_element_by_css_selector(self.login_in_css).click()
    def clicklogout(self):
        self.driver.find_element_by_xpath(self.login_out_xpath).click()
