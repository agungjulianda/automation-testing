import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from pageObjects.DcmPage import DCM 
from pageObjects.ErrorMessage import ErrorCatch
from pageObjects.OTPPage import OTP

import time
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen
from Utilities import excelUtils

class Test_004_ConnectNewAccounts:
    baseURL = readConfig.getAppURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    def_otp = readConfig.getdefOTP()
    path= "testCases\\TestData\\UserData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_CNA(self,setup):
        self.logger.info("***** Test Test_005_Connect New Account")
        self.logger.info("***** Verifying Connect New Account ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.ec = ErrorCatch(self.driver)
        self.dcm = DCM(self.driver)
        self.otp = OTP(self.driver)

        try:
            #self.rows = excelUtils.getRowCount(self.path , 'Sheet1')
            #self.user = excelUtils.readData(self.path, 'Sheet1' , 2 , 1)
            #self.password = excelUtils.readData(self.path, 'Sheet1' , 2 , 2)
            #self.exp = excelUtils.readData(self.path, 'Sheet1' , 2 , 3)

            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            
            self.dcm.clickonProfile()
            self.dcm.clickonDCM()
            self.dcm.clickonCard()
            self.dcm.clickonConAcc()
            
            time.sleep(3)
        
        except:
            
            error_mes = self.ec.getErrorMessage()
            self.logger.error("***** Connect New Account Failed ")
            self.logger.error(error_mes)
            self.driver.close()
            time.sleep(3)
            assert False
            

            
                

            


            
            
        
   
        
        