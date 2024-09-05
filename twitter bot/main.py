from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from userInfo import username,password

s = Service(r"C:\Program Files (x86)\chromedriver.exe")


time.sleep(2)
def twitter(self,username,password):
    self.driver = webdriver.Chrome(service=s)
    self.driver.get("https://twitter.com/")
    self.username = username
    self.password = password
    self.driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()
    
    


tw = twitter(username,password)
tw
