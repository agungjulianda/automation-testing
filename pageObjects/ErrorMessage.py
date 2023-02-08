from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ErrorCatch:
    
    
    error_page_xpath = "//*[@id='error-message-box']"
    error_id = "error-message-box"


    def __init__(self,driver):
        self.driver=driver
        
    def checkingError(self):
        status = False
        try:
            error_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.error_page_xpath)))

            status = True
            
        except:
            status = False

        return status

    def getErrorMessage(self):

        error_message = None
        while(error_message == None):
            error_message = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.error_page_xpath))).text
        
        

        return error_message