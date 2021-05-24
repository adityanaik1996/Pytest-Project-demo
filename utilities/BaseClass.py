
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "."))
import time as t
from datetime import date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.TestData import getProperty
from utilities.custom_logger import customLogger
import datetime

class BaseClass:
    log=customLogger()
    def __init__(self,driver):
        self.driver=driver



    def SwitchToWindow(self,WindowNumber):
        t.sleep(2)
        window_after = self.driver.window_handles[WindowNumber]
        self.driver.switch_to.window(window_after)


    def GetTheCurrentDate(self):
        today = date.today()
        date1 = today.strftime("%d/%m/%Y")
        self.log.info("Current Date = "+date1)
        return date1

    def GetNextDate(self,days=5):
        date = datetime.date.today() + datetime.timedelta(days)
        date2=date.strftime("%d/%m/%Y")
        return date2

    def ScrollTillTopOfThePage(self):
        self.driver.execute_script("window.scrollTo(0,0)")
        t.sleep(3)

    def ScrollTillEndOfThePage(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        t.sleep(2)

    def ScrollTillElementFound(self,Element):
        self.driver.execute_script("arguments[0].scrollIntoView();", Element)
        t.sleep(2)

    def ClickOnTheElementWhenDisplayed(self,WebElement):
        element=WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.XPATH,WebElement)))
        return element

    def ClickOnTheElementWhenEnabled(self,WebElement):
        element=self.driver.find_element(By.XPATH,WebElement).is_enabled()
        if element==True:
            self.driver.find_element(By.XPATH, WebElement).click()
        else:
            t.sleep(8)
            self.driver.find_element(By.XPATH, WebElement).click()

    def SwitchToFrame(self,Value):
        iframe = self.driver.find_element(By.ID,Value)
        self.driver.switch_to.frame(iframe)
        t.sleep(3)