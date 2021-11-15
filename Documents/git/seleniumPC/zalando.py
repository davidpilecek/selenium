from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

i=0

main = ('VaE1kV', 'C3wGFf', 'JT3_zV', 'adFHlH', '_0xLoFW', '_7ckuOK', 'mROyo1', '_1z5_Qg', 'U4aOaA')

item = ('_4qWUe8', 'w8MdNG', 'cYylcv', 'QylWsg', 'SQGpu8', 'iOzucJ', 'JT3_zV', 'DvypSJ')

text = ('_0mW-4D', '_0xLoFW', 'JT3_zV', 'mo6ZnF', '_78xIQ-', 'EJ4MLB', 'hPWzFB', 'u-6V88', 'ka2E9k', 'uMhVZi',
'FxZV-M', 'Kq1JPK', 'pVrzNP', 'ZkIJC-', 'r9BRio', 'qXofat', 'EKabf7', 'nBq1-s', '_2MyPg2')

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.zalando.cz/cepice-muzi/")

#U4aOaA

try:
     boxes = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.CLASS_NAME, "U4aOaA"))
     )

     products = boxes.find_elements_by_class_name("_4qWUe8.w8MdNG.cYylcv.QylWsg.SQGpu8.iOzucJ.JT3_zV.DvypSJ")
     for product in products:
        model = product.find_element_by_class_name("u-6V88.ka2E9k.uMhVZi.FxZV-M._6yVObe.pVrzNP.ZkIJC-.r9BRio.qXofat.EKabf7.nBq1-s._2MyPg2")
        brand = product.find_element_by_class_name("u-6V88.ka2E9k.uMhVZi.FxZV-M.Kq1JPK.pVrzNP.ZkIJC-.r9BRio.qXofat.EKabf7.nBq1-s._2MyPg2")
        print(brand.text)
        print(model.text)
        i = i+1
        print(i)
finally:
     driver.quit()




