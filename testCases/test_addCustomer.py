from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddcustomerPage import AddCustomer
class Test_003_AddCutomer:
    baseUrl=ReadConfig.getApplicationURL()
    username=ReadConfig.getEmail()
    password=ReadConfig.getpassword()
    logger=LogGen.loggen()

    def test_addCustomer(self,setup):
        self.logger.info("***********Test_003_AddCutomer*********")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.userName(self.username)
        self.lp.userpsw(self.password)
        self.lp.clicklogin()
        self.logger.info("*********Login Succesful*********")
        self.logger.info("*******Starting Add Customer Test*******")
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersItemMenu()
        self.addcust.addNewCustomer()

        self.logger.info("*******Providing Customer Info********")




