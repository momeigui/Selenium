# coding=UTF-8
#!/usr/bin/env python
from tomd import Tomd
import requests
import time
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('no-sandbox')
option.add_argument('disable-dev-shm-usage')
wd = webdriver.Chrome('/home/ubuntu/webdriver/chromedriver',chrome_options=option)
#启动浏览器驱动，同时启动浏览器
wd.implicitly_wait(10)
# 等待加载完毕后选取元素
wd.get("https://m.weibo.cn/u/1987241375")
#打开网址https://weibo.com/yoman77

def pullNewMessage():
   # 获取最新的微博，并返回最新消息
   wd.refresh()
   elements = wd.find_elements_by_class_name("weibo-og")
   return elements[1].text


def sendMessage(text):
   # 发送信息
   api = "https://sc.ftqq.com/SCU38515Tae77f4f7129fc5768ee87956955f31745c2a1df112db9.send"
   title = "又有新的优惠信息了"
   data = {
      "text":title,
      "desp":text
   }
   req = requests.post(api,data = data)

oldMessage = "初始化值"

# print(pullNewMessage())

while 1:
   time.sleep(5)
   t = pullNewMessage()
   if oldMessage != t:
      sendMessage(t)
      print(t)
      oldMessage = t
   




# sendMessage(text)

pass