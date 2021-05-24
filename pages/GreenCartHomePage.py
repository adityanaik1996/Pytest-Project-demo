import getpass
import time as t
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..."))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utilities.TestData import getProperty
import utilities.custom_logger as cl
from utilities.BaseClass import BaseClass
import logging
import pyodbc
import pandas as pd
import glob
from TestData.LoginData import Login

class GreenCartHomePageObjs():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.base=BaseClass(self.driver)
        self.driver.implicitly_wait(10)

    def SearchVegitables(self):
        return self.driver.find_element(By.CSS_SELECTOR,getProperty['SearchVegitable_Element'])

    def AddtoCartBtns(self):
        return self.driver.find_elements(By.XPATH,getProperty['AddtoCart_Btn'])

    def getAddItemCount(self):
        return self.driver.find_element(By.XPATH,getProperty['TotalItemcount'])


    def GetTheDetailsFromDB(self,sqlQuery):
        ServerName=Login['ServerName']
        DataBase_Name=Login['DataBase_Name']
        DB_UserName=Login['DB_UserName']
        DB_Password=Login['DB_Password']
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 11 for SQL Server};SERVER='+ServerName+';DATABASE='+DataBase_Name+';UID='+DB_UserName+';PWD='+DB_Password)
        DBvalue = pd.read_sql_query(sqlQuery, conn)
        ListOfValues = DBvalue[sqlQuery.split()[1]]
        ListOfValues2=[]
        for i in ListOfValues:
            ListOfValues2.append(i)
        return ListOfValues2



                