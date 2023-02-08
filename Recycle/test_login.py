import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from pageObjects.DcmPage import DCM
from pageObjects.ErrorMessage import ErrorCatch
import time
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen

class Test_001_login:
    baseURL = readConfig.getAppURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = LogGen.loggen()
    logger.info("===========================================================================================")
    def test_homePageTitle(self,setup):
        self.logger.info("***** Test Access URL")
        self.logger.info("***** Verifying Access URL ")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        
        if act_title == "D-Bank PRO":
            self.logger.info("***** Accessing URL Passed ")
            self.driver.close()
            time.sleep(3)
            assert True

        else:
            self.logger.error("***** Accessing URL Failed ")
            self.driver.close()
            time.sleep(3)
            assert False


    def test_login(self,setup):
        self.logger.info("***** Test Login ")
        self.logger.info("***** Verifying Login ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.ec = ErrorCatch(self.driver)
        status = self.ec.checkingError()

        if status == True:

            
            error_mes = self.ec.getErrorMessage()
            self.logger.error("***** Verifying Login Failed ")
            self.logger.error(error_mes)
            self.driver.close()
            time.sleep(3)
            assert False
            

        else:
            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            act_url = self.driver.current_url
            if act_url == "https://omni-pt.dbank.co.id/#/dashboard/home" :
                #self.lp.clickLogout()
                self.logger.info("***** Verifying Login Passed ")
                self.driver.close()
                time.sleep(3)
                assert True
                
                
            else:
                error_mes = self.ec.getErrorMessage()
                self.logger.error("***** Verifying Login Failed ")
                self.logger.error(error_mes)
                self.driver.close()
                time.sleep(3)
                assert False
            
        
    def testDCM(self,setup):

        self.logger.info("***** Test Navigate DCM ")
        self.logger.info("***** Verifying Navigate DCm ")
        self.driver = setup
        self.dc = DCM(self.driver)
        self.lp = Login(self.driver)
        self.driver.get(self.baseURL)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.dc.clickonProfile()
        self.dc.clickonDCM()
        time.sleep(3)
        status = self.dc.checkDCM()
        if status == True:
            self.logger.info("***** Verifying Navigate DCM Passed ")
            self.driver.close()
            time.sleep(3)
            assert True
        else:
            self.logger.error("***** Verifying Navigate DCM Failed ")
            self.driver.close()
            time.sleep(3)
            assert False
        
        