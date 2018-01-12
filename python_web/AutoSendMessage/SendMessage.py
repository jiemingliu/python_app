import time
from selenium.webdriver.common.keys import Keys

def sendMessage(driver,phone):
	#点击沟通
	goutong = driver.find_element_by_css_selector('.button.button-success')
	goutong.click()
	
	#输入电话
	photo_name = driver.find_element_by_css_selector("#chooseStudentSearchForm>div.row>div.controls>input")
	photo_name.click()
	photo_name.clear()
	photo_name.send_keys(phone)
	
	#点击查询
	chaxun = driver.find_element_by_css_selector("#chooseStudentSearchForm>div.row>div.controls>button[type='submit']")
	chaxun.click()
	
	time.sleep(2)
	
	#选中学员
	#xuanzhongxueyuan = driver.find_element_by_css_selector("#chooseStudentGrid>div.bui-grid.bui-simple-list.bui-grid-border.bui-grid-strip>div.bui-grid-body>")
	xuanzhongxueyuan = driver.find_element_by_css_selector('.bui-grid-radio')
	print(xuanzhongxueyuan)
	print(xuanzhongxueyuan.get_attribute('type'))
	xuanzhongxueyuan.send_keys(Keys.SPACE)
	
	#输入回复内容
	huifuneirong = driver.find_element_by_id('toContent')
	huifuneirong.click()
	huifuneirong.clear()
	huifuneirong.send_keys(u'再次恭喜拿照')
	
	#确认发送
	queren = driver.find_elements_by_css_selector('.bui-stdmod-footer>button')
	queren[0].click()
	print(queren[0].text)
		
	queren1 = driver.find_element_by_css_selector('.bui-message.bui-dialog.bui-overlay.bui-ext-position.x-align-cc-cc>.bui-stdmod-footer>button')
	queren1.click()
	
	time.sleep(1)