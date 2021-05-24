import logging
import pytest
import utilities.custom_logger as cl
import time as t
import sys
import os
from utilities.BaseClass import BaseClass
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..."))
from pages.GreenCartHomePage import GreenCartHomePageObjs


@pytest.mark.usefixtures("setup")
class TestAddAndValidateItemsInCart():
    log = cl.customLogger(logging.DEBUG)

    def test_AddItemsToCart(self):
        global homePage,TotalitemsAdded
        baseclass = BaseClass(self.driver)
        homePage = GreenCartHomePageObjs(self.driver)
        homePage.SearchVegitables().click()
        t.sleep(2)
        homePage.SearchVegitables().send_keys("br")
        t.sleep(4)
        AddItemtoCart=homePage.AddtoCartBtns()
        TotalitemsAdded=len(AddItemtoCart)
        print(TotalitemsAdded)
        for button in AddItemtoCart:
            button.click()

    def test_ValidateTheItemInCart(self):
        totalItems=int(homePage.getAddItemCount().text)
        print(totalItems)
        assert TotalitemsAdded==totalItems



