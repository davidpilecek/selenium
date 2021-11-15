from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome("C:\Users\David\Downloads\chromedriver.exe")

driver.get("https://www.zalando.cz/cepice-muzi/")

link = driver.find_element_by_partial_link_text("Klobouky")
link.click()

try:
     element = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "GANT"))
     )
     
     element.click()
     

except:
     driver.quit()