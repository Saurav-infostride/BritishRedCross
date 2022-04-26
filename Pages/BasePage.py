
from asyncio import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''This class is the parent of all pages'''
'''It contains all generic methods and utitlities for all the pages'''

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self):
        return self.driver.title

    def if_alert(self):
        elements = self.driver.find_elements_by_xpath("//button[text()='Accept Cookies']")
        if not elements:
            print("No element found")  
        else:
            self.driver.find_element_by_xpath("//button[text()='Accept Cookies']").click()

    def validate_product(product):
        if product < 0:
            raise ValueError("Product is not available")
    


    
        