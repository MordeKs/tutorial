# -*- encoding: utf-8 -*-
"""
@File    : save_cookies.py
@Time    : 2020/8/11 10:55
@Author  : Morde
@Software: PyCharm
@Description: 保存登录的cookie
"""

import time
import json
import redis
from selenium import webdriver

client = redis.StrictRedis()
url = ''
driver = webdriver.Chrome()
driver.get(url)
user = driver.find_element_by_xpath('')
user.clear()
user.send_keys('user')

password = driver.find_element_by_xpath('')
password.clear()
password.send_keys('pwd')

remember = driver.find_element_by_xpath('')
remember.clear()

login = driver.find_element_by_xpath('')
login.click()
time.sleep(2)
cookies = driver.get_cookies()
client.lpush('cookies',json.dumps(cookies))
driver.quit()

