from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytesseract
from PIL import Image

image_url = r"http://cloud.jiabenyi.com/admin/auth/code.htm?key=4ea8e987-c9ef-4a7a-99d1-591a34ec74bb"
driver_url = r"D:\Tools\driverTools\chromedriver.exe"
network_url = r'http://cloud.jiabenyi.com/admin'

driver = webdriver.Chrome(driver_url)
driver.get(network_url)
print(driver.title)
mobile = driver.find_element_by_id('mobile')
print(mobile)
mobile.click()
mobile.send_keys(13545236105)
pwd = driver.find_element_by_id('pwd')
pwd.click()
pwd.send_keys(666666)



image = Image.open(image_url)
vcode = pytesseract.image_to_string(image)
code = driver.find_element_by_id('code')
pwd.click()
code.send_keys(vcode)
#id1 = driver.find_element_by_class('nav-item-inner nav-eachinfo')
#print(id1)