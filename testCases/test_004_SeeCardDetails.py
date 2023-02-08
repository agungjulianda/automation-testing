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

class Test_004_SeeCardDetails:
    baseURL = readConfig.getAppURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    def_otp = readConfig.getdefOTP()
    path= "testCases\\TestData\\UserData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_SDC(self,setup):
        self.logger.info("***** Test Test_004_See Card Details ")
        self.logger.info("***** Verifying See Card Details ")
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
            self.dcm.clickonSCD()
            time.sleep(2)

            self.otp.setOTP(self.def_otp)
            self.otp.clickonSubmit()
            time.sleep(3)
            status = self.dcm.checkSDCTimer()

            if status == True:
                self.logger.info("***** See Card Details Passed ")
                self.driver.close()
                assert True

            else:
                self.logger.info("***** See Card Details Failed ")
                self.driver.close()
                assert False
        
        except:
            
            error_mes = self.ec.getErrorMessage()
            self.logger.error("***** See Card Details Failed ")
            self.logger.error(error_mes)
            self.driver.close()
            time.sleep(3)
            assert False

            


            
            
        
   
        
        