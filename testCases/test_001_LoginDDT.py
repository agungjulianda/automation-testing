import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from pageObjects.DcmPage import DCM
from pageObjects.ErrorMessage import ErrorCatch
import time
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen
from Utilities import excelUtils

class Test_001_login_DDT:
    baseURL = readConfig.getAppURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    path= "testCases\\TestData\\UserData.xlsx"

    logger = LogGen.loggen()

    def test_login(self,setup):
        self.logger.info
        self.logger.info("***** Test Test_001_login_DDT ")
        self.logger.info("***** Verifying test_login ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.ec = ErrorCatch(self.driver)
        
        try:
            #self.rows = excelUtils.getRowCount(self.path , 'Sheet1')
            #self.user = excelUtils.readData(self.path, 'Sheet1' , 2 , 1)
            #self.password = excelUtils.readData(self.path, 'Sheet1' , 2 , 2)
            #self.exp = excelUtils.readData(self.path, 'Sheet1' , 2 , 3)

            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            expected_url = "https://omni-pt.dbank.co.id/#/dashboard/home"
            act_url = self.driver.current_url
            if act_url == expected_url :
                self.logger.info("***** Verifying Login Passed ")
                self.lp.clickLogout()
                self.driver.close()
                assert True
                
                
            else:
                error_mes = self.ec.getErrorMessage()
                self.logger.error("***** Verifying Login Failed ")
                self.logger.error(error_mes)
                self.driver.close()
                assert False
            
        except:
            
            error_mes = self.ec.getErrorMessage()
            self.logger.error("***** Verifying Login Failed ")
            self.logger.error(error_mes)
            self.driver.close()
            time.sleep(3)
            assert False
        
   
        
        