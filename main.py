import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from openpyxl import Workbook, load_workbook

import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://emn178.github.io/online-tools/sha256.html"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.ID, "input")
find.send_keys("Sample text")

find = driver.find_element(By.ID, "output")
temp = find.get_attribute("value")
temp2 = find.get_attribute("placeholder")
print(temp2)

input()