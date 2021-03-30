# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 20:47
# @Author  : cyx
# @function: 该功能描述
# @gitbub  :
"""
作业：通过浏览器利用cookie实现企业微信登录
解题思路：
第一种方法、通过复用浏览器登录企业微信，（顺便获取用户cookie）
1）登录企业微信
2）打开复用浏览器的方法：cmd命令行窗口：chrome -remote-debugging-port=9222（执行命令前，关闭所有chrome）
3) 复用浏览器参数：webdriver.ChromeOptions.debugger_address = '127.0.0.1:9222'
4）打开复用浏览器： webdriver.Chrome(options=上面参数)
5）打开有登录态的企业微信，并获取用户cookie，并记录到文本中【ps: 如果想cookie能够长期使用，可以修改cookie的有效时间】
第二种方法、取存在的cookie添加到请求中，驱动浏览器打开企业微信，刷新页面，实现利用cookie登录企业微信
1）打开浏览器
2）从文件中读取cookie，并添加到请求中
3）去登录企业微信，登录成功，则实现了cookie登录；否则debug排查代码

"""
import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    # # 第一种方法：复用浏览器,（顺便把cookie存下来）
    # def test_get_cookie(self):
    #     "复用浏览器,并把cookie存下来"
    #     Firefox_arg = webdriver.FirefoxOptions()
    #     Firefox_arg.debugger_address = '127.0.0.1:9222'
    #     self.driver = webdriver.Firefox(options=Firefox_arg)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     sleep(15)
    #     self.driver.find_element_by_id("menu_apps").click()
    #     sleep(3)
    #     cookie = self.driver.get_cookies()
    #     print(cookie, type(cookie))
    #     with open("./cookie.txt", 'w', encoding="utf-8") as f:
    #         json.dump(cookie, f)

    # 第二种方法：打开浏览器，手动扫码登录，获取cookie存起来，利用cookie登录
    def test_cookie_login(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(15)  # 此处登录cookie
        self.driver.find_element_by_id("menu_apps").click()
        sleep(3)
        cookie = self.driver.get_cookies()
        print(cookie, type(cookie))
        with open("./cookie.txt", 'w', encoding="utf-8") as f:
            json.dump(cookie, f)
        try:
            with open('./cookie.txt', 'r', encoding='utf-8') as f:
                cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            "登录后的操作"
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "menu_customer")))
            self.driver.find_element_by_id("menu_customer").click()
        finally:
            sleep(3)
            self.driver.quit()