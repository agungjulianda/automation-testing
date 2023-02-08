import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from pageObjects.DcmPage import DCM 
from pageObjects.ErrorMessage import ErrorCatch
from pageObjects.OTPPage import OTP
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
        self.logger.info("***** Test Test_006_Delete Connected Account")
        self.logger.info("***** Verifying Delete Connected Account ")
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
            self.account1 = len(self.driver.find_elements(By.CLASS_NAME,"card"))
            if self.account1 == 1:
                self.logger.error("***** Delete Connected Account Failed ")
                self.logger.error("***** Delete Connected Account Failde : Test Data Invalid ")
                self.driver.close()
                assert False
                

            else:
                self.dcm.clickonDeleteAcc()
                time.sleep(3)
                self.otp.setOTP(self.def_otp)
                self.otp.clickonSubmit()
                time.sleep(3)
                self.dcm.clickonOkbutton()
                self.dcm.clickonCard()
                self.dcm.clickonConAcc()
                time.sleep(3)
                account2 = len(self.driver.find_elements(By.CLASS_NAME,"card"))
                time.sleep(3)

                if self.account1 > account2:
                    self.logger.info("***** Delete Connected Account Passed ")
                    self.driver.close()
                    assert True
                
                else:
                    self.logger.error("***** Delete Connected Account Failed ")
                    self.driver.close()
                    assert False
        
        except:
            
            error_mes = self.ec.getErrorMessage()
            self.logger.error("***** Delete Connected Account Failed ")
            self.logger.error(error_mes)
            self.driver.close()
            time.sleep(3)
            assert False
            

            
                

            


            
            
        
   
        
        