"""
Auto-Typing Script for Typing Practice
Copyright (c) 2025 WanDaiser
Licensed under Custom Software License - see LICENSE file
Contact: salihefeggl@gmail.com
"""

import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.m5bilisim.com/tr/on-parmak/calisma/kelime/?m=46")
time.sleep(0.00001)

i = 1


while i < 3000:
    gc = driver.find_element(By.ID, "yaziyaz")
    gv = driver.find_elements(By.XPATH, "//*[@id='satir']/span[" + str(i) + "]")
    if gv:
        gc.send_keys(gv[0].text + " ")
    i += 1
    time.sleep(0.00001)
driver.quit()
