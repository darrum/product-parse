import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

from openpyxl import Workbook, load_workbook

wb = load_workbook('WIEBETECH PRICES.xlsx')
ws = wb.active
max_row = ws.max_row
total = 0

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://emn178.github.io/online-tools/sha256.html"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.LINK_TEXT, "SHA224")
find.click()
delay = 2
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "input")))
print("objekts ir uz ekrana")
input()