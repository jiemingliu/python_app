# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytesseract
from PIL import Image
from SendMessage import sendMessage
import time
import xlrd

ex = xlrd.open_workbook(r'test.xlsx')
sheet1 = ex.sheet_by_index(0)
cCols = sheet1.col_values(2)
for i in cCols:
	print(i)

driver_url = r"D:\Tools\driverTools\chromedriver.exe"
network_url = r'http://cloud.jiabenyi.com/admin'

driver = webdriver.Chrome(driver_url)
driver.get(network_url)
mobile = driver.find_element_by_id('mobile')
mobile.click()
mobile.send_keys(13545236105)
pwd = driver.find_element_by_id('pwd')
pwd.click()
pwd.send_keys(666666)

time.sleep(10)

code = driver.find_element_by_id('code')
f = open('VerificationCode.txt','r')
codeStr = f.read()
code.click()
code.send_keys(codeStr)

newButton = driver.find_element_by_id('newbutton')
newButton.click()

# time.sleep(2)

# current_url = driver.current_url
# left_url = current_url.split('#')[0]
# whole_url = left_url+'/#sys_feedback/carConsulting'
# print(whole_url)
# driver.get(whole_url)

time.sleep(2)

goutong_url = r'http://cloud.jiabenyi.com/admin/system/carConsulting.htm'
driver.get(goutong_url)

time.sleep(2)



sendMessage(driver,13618615940)