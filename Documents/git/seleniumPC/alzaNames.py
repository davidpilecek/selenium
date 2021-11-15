from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.alza.cz/true-wireless-sluchatka/18864672.htm")

#U4aOaA

try:
     boxes = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.ID, "boxc"))
     )

     products = boxes.find_elements_by_class_name("box")
     for product in products:
        item = product.find_element_by_class_name("name")
        print(item.text)
finally:
     driver.quit()

#right_arrow.send_keys(Keys.RETURN)

#right_arrow = driver.find_element_by_class_name("DJxzzA.PgtkyN")





