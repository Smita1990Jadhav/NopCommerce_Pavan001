import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


class AddCustomer:
    lnkCutomer_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCutomers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnewCust_xpath="//a[@href='/Admin/Customer/Create']"
    txtEmail_xpath="//input[@name='Email']"
    txtPassword_xpath="//input[@name='Password']"
    txtFirstname_xpath="//input[@name='FirstName']"
    txtLastname_xpath="//input[@name='LastName']"
    rdMalegenderidclick_xpath="//input[@id='Gender_Male']"
    rdFemalegenderidclick_xpath="//input[@id='Gender_Female']"
    txtDOB_xpath="//input[@id='DateOfBirth']"
    txtCompanyname_xpath="//input[@id='Company']"
    ChkboxtaxCLK_xpath="//input[@id='IsTaxExempt']"
    txtNewletter_xpath="//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']"
    txtCustomerRole_xpath="//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrator_xpath="//li[contains(text(),'Administrators')]"
    lstitemForumModerator_xpath="//li[contains(text(),'Forum Moderators')]"
    lstitemGuest_xpath="//li[contains(text(),'Guests')]"
    lstitemRegistered_xpath="//li[contains(text(),'Registered')]"
    lstitemsVendors_xpath="//li[contains(text(),'Vendors')]"
    drpmgrVendor_xpath="//*[@id='VendorId']"
    chkboxClickActive_xpath="//input[@id='Active']"
    txtAdminComment_xpath="//*[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCutomer_menu_xpath).click()

    def clickOnCustomersItemMenu(self):
        self.driver.find_element_by_xpath(self.lnkCutomers_menuitem_xpath).click()

    def addNewCustomer(self):
        self.driver.find_element_by_xpath(self.btnAddnewCust_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setfirstName(self,fname):
        self.driver.find_element_by_xpath(self.txtFirstname_xpath).send_keys(fname)

    def setlastName(self,lname):
        self.driver.find_element_by_xpath(self.txtLastname_xpath).send_keys(lname)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element_by_xpath(self.rdMalegenderidclick_xpath).click()
        elif gender=='Female':
            self.driver.find_element_by_xpath(self.rdFemalegenderidclick_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rdMalegenderidclick_xpath).click()

    def setDOB(self,dob):
        self.driver.find_element_by_xpath(self.txtDOB_xpath).send_keys(dob)

    def compName(self,compname):
        self.driver.find_element_by_xpath(self.txtCompanyname_xpath).send_keys("CloudCodes NON Commerce")
    def taxcheckboxClk(self):
        self.driver.find_element_by_xpath(self.ChkboxtaxCLK_xpath).click()

    def setCustRole(self,role):#need to call this method two times if want to select multiple roles.
        self.driver.find_element_by_xpath(self.txtCustomerRole_xpath).click()
        time.sleep(3)
        if role=='Registered':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)

        elif role=='Administrator':
            self.driver.find_element_by_xpath(self.lstitemAdministrator_xpath)

        elif role=="Guest":
            time.sleep()
            self.driver.find_element_by_xpath("//ul[@id='SelectedCustomerRoleIds_taglist']//span[contains(text(),'Registered')]").click()
            self.driver.find_element_by_xpath(self.lstitemGuest_xpath)
        elif role=='Registered':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)

        elif role=='Vendors':
            self.listitem =self.driver.find_element_by_xpath(self.lstitemsVendors_xpath)

        else:
            self.listitem =self.driver.find_element_by_xpath(self.lstitemGuest_xpath)
            time.sleep(3)
            #self.listitem.click()->It will not work so we use below java script statement.
            self.driver.execute_script("arguments[0].click();",self.listitem)

    def setMgrVendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.drpmgrVendor_xpath))
        drp.select_by_visible_text(value)

    def chkCheckbox(self):
        self.driver.find_element_by_xpath(self.chkboxClickActive_xpath).click()

    def setAdminComment(self,admincomment):
        self.driver.find_element_by_xpath(self.txtAdminComment_xpath).send_keys(admincomment)

    def clickSaveButton(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()




