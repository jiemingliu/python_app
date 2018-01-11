from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytesseract
from PIL import Image
import time

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

time.sleep(10)

code = driver.find_element_by_id('code')
f = open('test.txt','r')
codeStr = f.read()
code.click()
code.send_keys(codeStr)

newButton = driver.find_element_by_id('newbutton')
newButton.click()

time.sleep(2)

current_url = driver.current_url
left_url = current_url.split('#')[0]
whole_url = left_url+'/#sys_feedback/carConsulting'
print(whole_url)
driver.get(whole_url)

goutong = driver.find_element_by_css_selector('button button-success')
print(goutong)
print(goutong.tag_name)

# zixun = driver.find_element_by_class_name('nav-item-inner nav-eachinfo')
# zixun.click()

# time.sleep(2)

# xuechezixun = driver.find_element_by_id('carConsulting')
# xuechezixun.click()

#codeImg = driver.find_element_by_id('codeImg')
#image_url = codeImg.get_attribute('src')
#print(image_url)
#im = Image.open('code.jpg')
#stri = pytesseract.image_to_string(im)






#id1 = driver.find_element_by_class('nav-item-inner nav-eachinfo')
#print(id1)