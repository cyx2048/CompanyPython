# -*-coding:utf-8-*-
# appium连接手机 安装重启qq
from appium import webdriver
import time

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='HUAWEI Mate 8'
desired_caps['platformVersion']='8.0.0'
desired_caps['udid']='5LM0216519002620'    #连接真机必须要有，唯一差别
desired_caps['automationName']='uiautomator2' #toast提示

# desired_caps['app']=r'D:\11\qq_1392.apk'
desired_caps['noReset'] = 'True'           #不需要清理数据，避免重新安装的问题
desired_caps['appPackage']='com.yyfax.app'
desired_caps['appActivity']='com.yyfax.app.main.launch.view.LaunchActivity'

print(desired_caps)
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(3)

# driver.find_element_by_link_text("登录/注册").click()
# driver.find_element_by_link_text("输入登录密码").send_keys("a123456")
# driver.find_element_by_link_text("•••••••, 输入登录密码").click()
# driver.find_element_by_link_text("登录").click()