#Testing Github
import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getEmail()
    password=ReadConfig.getpassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("*******************Test_001_Login***********************")
        self.logger.info("***************************Verifying Home Page Title***************************")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        #self.driver.close()
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********************Home Page title page Test pass**********************")
        else:
            self.driver.save_screenshot('D:\\pythonProject\\nopcommerceApp\\Screenshots\\homePageTitle.png')
            self.driver.close()
            self.logger.error("********************************Home Page Title Page Test Fail************************************")
            assert False




    def test_login(self,setup):
        self.driver =setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.userName(self.username)
        self.lp.userpsw(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        print(act_title)
        #self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('D:\\pythonProject\\nopcommerceApp\\Screenshots\\login.png')
            self.driver.close()
            assert False
