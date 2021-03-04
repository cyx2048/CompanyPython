# -*-coding:utf-8-*-
# appium连接模拟器 安装重启qq
from appium import webdriver
import  time

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:21503'
desired_caps['platformVersion']='7.1.2'

desired_caps['app']=r'D:\360浏览器\yyfax_6.0.1_debug_1497_141.apk'
desired_caps['noReset'] = 'True'           #不需要清理数据，避免重新安装的问题
desired_caps['appPackage']='com.tencent.mm'
desired_caps['appActivity']='com.tencent.mm.ui.LauncherUI'
desired_caps['unicodeKeyboard']=True   #是使用unicode编码方式发送字符串
desired_caps['resetKeyboard']=True     #隐藏键盘

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(30)

driver.find_element_by_id("com.tencent.mm:id/f0f").click()
time.sleep(8)
driver.find_element_by_android_uiautomator('new UiSelector().text("搜索")').send_keys("传奇哥")
time.sleep(2)
driver.find_element_by_android_uiautomator('new UiSelector().text("传奇哥")').click()

time.sleep(5)
driver.find_element_by_id("com.tencent.mm:id/g2t").click()
driver.find_element_by_class_name("android.widget.EditText").send_keys("爱你")
driver.find_element_by_android_uiautomator('new UiSelector().text("发送")').click()

i=0
while(i<100):
    i = i + 1
    driver.find_element_by_class_name("android.widget.EditText").send_keys("爱你")
    driver.find_element_by_android_uiautomator('new UiSelector().text("发送")').click()