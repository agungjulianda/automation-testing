from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Utilities.readProperties import readConfig
from selenium.webdriver.support.ui import Select

class LCA:
  
    accnumb = readConfig.getAccoutNumberCNA()
    con_acc_xpath = "//*[@id='holder']/card-view/div[1]/div/div[4]/div/div/div/div/div[3]/div/div[1]"
    dltbtn_xpath = "//*[@class='arrowimg']" 
    okbtn_xpath = "//*[@class='btn btn-primary lanjut-btn ok']"
    cnanextbtn_xpath = "//*[@class='btn btn-primary lanjut-btn']"
    addacc_xpath = "//*[@class='btn btn-primary lanjut-btn']"
    dropdown_xpath = "//*[@class='btn dropdown-toggle btn-light']"
    accnumb_xpath =f"//*[@class='text' and contains(text(),{accnumb})]"
    chckbox_xpath = "//*[@type = 'checkbox']"
 

    def __init__(self,driver):
        self.driver=driver

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
        
    def clickonaddAccount(self):
        addacc_xpath = None
        while(addacc_xpath == None):
            addacc_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.addacc_xpath)))
        
        time.sleep(5)
        addacc_xpath.click()  

    def clickonDropdown(self):
        dropdown_xpath = None
        while(dropdown_xpath == None):
            dropdown_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.dropdown_xpath)))
        
        time.sleep(5)
        dropdown_xpath.click()  
    
    def sellectAccount(self):
        accnumb_xpath = None
        while(accnumb_xpath == None):
            accnumb_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.accnumb_xpath)))
        time.sleep(5)   

        #accnumb_xpath.click()


    def clickonNextCNA(self):
        nextbutton_xpath = None
        while(nextbutton_xpath == None):
            nextbutton_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.cnanextbtn_xpath)))
        
        time.sleep(5)
        nextbutton_xpath.click()  

    def checktncBox(self):
        tncbox_xpath = None
        while(tncbox_xpath == None):
            tncbox_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.chckbox_xpath)))
        
        time.sleep(5)
        tncbox_xpath.click()

    def clickonOkbutton(self):
        okbtn_xpath = None
        while(okbtn_xpath == None):
            okbtn_xpath = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.XPATH, self.okbtn_xpath)))
        
        
        time.sleep(5)
        okbtn_xpath.click() 

    

