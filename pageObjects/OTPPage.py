from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class OTP:
  

    menu_profile_xpath = "//*[@id='header']/div/div[2]/ul/li[4]"
    menu_dcm_xpath = "//*[@id='holder']/profile/div[2]/div/form/div[2]/div[4]"
    cardlist_xpath = "//*[@id='account-tab']/div/div/div"
    card_xpath = "//span[contains(text(),'5953')]"
    sdc_xpath = "//button[@class = 'col-md-3 activebutton lihat-btn']"
    otpbox_id = "otp"
    submit_xpath = "//button[@type = 'submit']"

    
    def __init__(self,driver):
        self.driver=driver

    
    def setOTP(self,def_otp):
        #username_box = self.driver.find_element(By.ID, self.textbox_username_id)
        otp_box = None
        while(otp_box == None):
            otp_box = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.ID, self.otpbox_id)))
        

        otp_box.send_keys(def_otp)

        otp_box.submit()

    def clickonSubmit(self):
        submit_xpath = None
        while(submit_xpath == None):
            submit_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.submit_xpath)))
        
        
        time.sleep(5)
        submit_xpath.click() 
