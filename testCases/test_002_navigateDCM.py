import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from pageObjects.DcmPage import DCM
from pageObjects.ErrorMessage import ErrorCatch
import time
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen
from Utilities import excelUtils

class Test_002_navigateDCM:
    baseURL = readConfig.getAppURL()
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    path= "testCases\\TestData\\UserData.xlsx"

    logger = LogGen.loggen()
    


    def test_navigateDCM(self,setup):
        self.logger.info
        self.logger.info("***** Test Test_002_Havigate DCM ")
        self.logger.info("***** Verifying Navigate DCM ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.ec = ErrorCatch(self.driver)
        self.dcm = DCM(self.driver)

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
            self.logger.info("***** Navigate DCM Passed ")
            time.sleep(3)
            self.driver.close()

        except:

            error_mes = self.ec.getErrorMessage()
            self.logger.error("***** Navigate DCM Failed ")
            self.logger.error(error_mes)
            self.driver.close()
            time.sleep(3)
            assert False
            


            
            
        
   
        
        