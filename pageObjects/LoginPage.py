from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Login:
    textbox_username_id = "username"
    textbox_password_id = "password"

    button_login_xpath = "//button[@type='submit']"
    button_logout_xpath = "/html/body/div/div/div[4]/div[1]/div/div[3]/div/div[2]/div"
    menu_home_xpath = "//*[@id='header']/div/div[2]/ul/li[1]"
    menu_profile_xpath = "//*[@id='header']/div/div[2]/ul/li[4]"
    error_page_xpath = "//*[@id='error-message-box']"
    error_id = "error-message-box"


    def __init__(self,driver):
        self.driver=driver


    def setUsername(self,username):
        #username_box = self.driver.find_element(By.ID, self.textbox_username_id)
        username_box = None
        while(username_box == None):
            username_box = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.ID, self.textbox_username_id)))
        

        username_box.send_keys(username)

        username_box.submit()


    def setPassword(self,password):
        #pasword_box = self.driver.find_element(By.ID, self.textbox_password_id)
        password_box = None
        while(password_box == None):
            password_box = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.ID, self.textbox_password_id)))

        password_box.send_keys(password)

        password_box.submit()


    def clickLogin(self):
        #self.driver.find_element_by_xpath(self.button_login_xpath).click()
        loginbtn_xpath = None
        while(loginbtn_xpath == None):
            loginbtn_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.button_login_xpath)))
        
        
        time.sleep(3)
        loginbtn_xpath.click()
        
    def clickonHome(self):
        homebtn_xpath = None
        while(homebtn_xpath == None):
            homebtn_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.menu_home_xpath)))
        
        
        time.sleep(3)
        homebtn_xpath.click()   
    
    def clickonProfile(self):
        profilebtn_xpath = None
        while(profilebtn_xpath == None):
            profilebtn_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.menu_profile_xpath)))
        
        
        time.sleep(3)
        profilebtn_xpath.click()   


    def clickLogout(self):
        #self.driver.find_element_by_xpath(self.button_logout_xpath).click()
        logoutbtn_xpth = None
        while(logoutbtn_xpth == None):
            logoutbtn_xpth = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.button_logout_xpath)))

        time.sleep(3)
        logoutbtn_xpth.click()
        
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