from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Utilities.readProperties import readConfig

class DCM:
  
    cardNumber = readConfig.getcardNumber()
    menu_profile_xpath = "//*[@id='header']/div/div[2]/ul/li[4]"
    menu_dcm_xpath = "//*[@id='holder']/profile/div[2]/div/form/div[2]/div[4]"
    cardlist_xpath = "//*[@id='account-tab']/div/div/div"
    card_xpath = f"//span[contains(text(),{cardNumber})]"
    sdc_xpath = "//button[@class = 'col-md-3 activebutton lihat-btn']"
    timer_xpath = "//*[@class = 'timer']"
    con_acc_xpath = "//*[@id='holder']/card-view/div[1]/div/div[4]/div/div/div/div/div[3]/div/div[1]"
    dltbtn_xpath = "//*[@class='arrowimg']" 
    okbtn_xpath = "//*[@class='btn btn-primary lanjut-btn ok']"
 

    def __init__(self,driver):
        self.driver=driver


     
    def clickonProfile(self):
        profilebtn_xpath = None
        while(profilebtn_xpath == None):
            profilebtn_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.menu_profile_xpath)))
        
        
        time.sleep(5)
        profilebtn_xpath.click()   

    def clickonDCM(self):
        dcmbtn_xpath = None
        while(dcmbtn_xpath == None):
            dcmbtn_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.menu_dcm_xpath)))
        
        
        time.sleep(5)
        dcmbtn_xpath.click()  

    def clickonCard(self):
        card_xpath = None
        while(card_xpath == None):
            card_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.card_xpath)))
        
        
        time.sleep(5)
        card_xpath.click()  

    def clickonSCD(self):
        sdc_path = None
        while(sdc_path == None):
            sdc_path = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.sdc_xpath)))
        
        
        time.sleep(5)
        sdc_path.click()  
    
    def clickonConAcc(self):
        conacc_xpath = None
        while(conacc_xpath == None):
            conacc_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.con_acc_xpath)))
        
        
        time.sleep(5)
        conacc_xpath.click()  
    
    def clickonDeleteAcc(self):
        deletacc_xpath = None
        while(deletacc_xpath == None):
            deletacc_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.dltbtn_xpath)))
        
        
        time.sleep(5)
        deletacc_xpath.click()  

    def clickonOkbutton(self):
        okbtn_xpath = None
        while(okbtn_xpath == None):
            okbtn_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.okbtn_xpath)))
        
        
        time.sleep(5)
        okbtn_xpath.click() 

    def checkDCM(self):
        status = False
        try:
            cardlist_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.cardlist_xpath)))

            status = True
            
        except:
            status = False

        return status
        
    def checkSDCTimer(self):
        status = False
        try:
            timer_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.timer_xpath)))

            status = True
            
        except:
            status = False

        return status
        
