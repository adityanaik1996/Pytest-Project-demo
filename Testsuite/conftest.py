import pytest
from selenium import webdriver
import sys
import os
import time as t
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "."))
from TestData.LoginData import Login
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager



@pytest.fixture(scope="class",params=Login["Browser"])
def setup(request):
    global driver
    if request.param=="Chrome":
        options = webdriver.ChromeOptions()
        #options.add_argument("headless")
        options.add_experimental_option('useAutomationExtension', False)
        capabilities = {'chromeOptions': {'useAutomationExtension': False,
                                              'args': ['--disable-extensions']}
                            }


        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif request.param=="Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Ie(IEDriverManager().install())

    driver.get(Login['URL'])
    driver.maximize_window()
    t.sleep(5)
    request.cls.driver=driver
    yield
    driver.quit()

