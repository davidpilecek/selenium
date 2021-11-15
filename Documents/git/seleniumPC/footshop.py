from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.footshop.cz/cs/4600-panske-tenisky")

#U4aOaA

try:
     main = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.CLASS_NAME, "GridListing_container_3DMdD"))
     )

     products = main.find_elements_by_class_name("Product_info_2vPxZ")
     for product in products:
        item = product.find_element_by_class_name("Product_name_17mav")
        text = item.text
        returned = text.find("adidas Stan Smith")
        if returned != -1:
            print(text)
            print(returned)
        


finally:
     driver.quit()



