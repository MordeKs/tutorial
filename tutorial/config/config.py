# -*- encoding: utf-8 -*-
"""
@File    : config.py
@Time    : 2020/8/11 8:56
@Author  : Morde
@Software: PyCharm
@Description:
"""

import os

import yaml

ENV = os.getenv('ENV', 'dev')

if ENV == 'pro':
    filename = 'pro.yml'
else:
    filename = 'dev.yml'

confpath = os.path.join(os.path.dirname(__file__), filename)

with open(confpath, 'r', encoding='utf8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

client = config['MongoDB']['client']

PROXIES = ['http://10.2.1.31:8070']

USER_AGENT_LIST = [
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
  "Dalvik/1.6.0 (Linux; U; Android 4.2.1; 2013022 MIUI/JHACNBL30.0)",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "AndroidDownloadManager",
  "Apache-HttpClient/UNAVAILABLE (java 1.4)",
  "Dalvik/1.6.0 (Linux; U; Android 4.3; SM-N7508V Build/JLS36C)",
  "Android50-AndroidPhone-8000-76-0-Statistics-wifi",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.4; MI 3 MIUI/V7.2.1.0.KXCCNDA)",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.2; Lenovo A3800-d Build/LenovoA3800-d)",
  "Lite 1.0 ( http://litesuits.com )",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
  "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; HTC T528t Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypay,securityinstalled); 360(android,uppayplugin); 360 Aphone Browser (2.0.4)",
]