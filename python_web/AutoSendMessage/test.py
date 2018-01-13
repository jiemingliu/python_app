# -*- coding:utf-8 -*-

import pytesseract
import sys,time
from PIL import Image,ImageEnhance
from selenium import webdriver

# driver_url = r"D:\Tools\driverTools\chromedriver.exe"
# network_url = r'http://cloud.jiabenyi.com/admin'

# driver = webdriver.Chrome(driver_url)
# driver.get(network_url)
# driver.get_screenshot_as_file('shot.png')
# im = Image.open('shot.png')
# box = (558,344,632,376)
# region = im.crop(box)
# region.save('code1.png')

# im = Image.open('code1.png')
# img = im.convert('L')
# sharp = ImageEnhance.Contrast(img)
# sharp1 = sharp.enhance(2.0)
# sharp1.save('code1.png')

code = pytesseract.image_to_string(Image.open('code.jpg'))

print("code=%s" % code)

# mobile = driver.find_element_by_id('mobile')
# mobile.click()
# mobile.send_keys(13545236105)
# pwd = driver.find_element_by_id('pwd')
# pwd.click()
# pwd.send_keys(666666)