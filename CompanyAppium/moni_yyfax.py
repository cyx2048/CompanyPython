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
desired_caps['appPackage']='com.yyfax.app'
desired_caps['appActivity']='com.yyfax.app.main.launch.view.LaunchActivity'
desired_caps['unicodeKeyboard']=True   #是使用unicode编码方式发送字符串
desired_caps['resetKeyboard']=True     #隐藏键盘

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(15)

driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("登录/注册")').click()
time.sleep(2)
driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("密码登录")').click()
time.sleep(2)

driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("输入邮箱或手机号")').click()

driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("输入邮箱或手机号")').clear()
driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("输入邮箱或手机号")').send_keys("3123")

driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("输入邮箱或手机号")').send_keys("1232")


driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("登录")').click()
