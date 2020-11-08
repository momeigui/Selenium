from selenium import webdriver

wd = webdriver.Chrome(r"E:\Documents\MYcode\selenium\chromedriver\chromedriver.exe")
#启动浏览器驱动，同时启动浏览器

wd.get("http://amor.spem.site")
#打开网址

# element = wd.find_element_by_id("kw")
#通过id查找元素，并返回web element对象

# element.send_keys("好好学习\n")
#输入字符串 按下回车

y = wd.find_element_by_class_name("h2")
print(y)

# element = wd.find_element_by_id("su")
# #选中搜索元素
# element.click()
# #点击元素

time.sleep(1)
#等待1秒

wd.implicitly_wait(10) 

pass