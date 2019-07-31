from selenium import webdriver
import time

driver = webdriver.Chrome()

#调整浏览器窗口的大小
driver.maximize_window() #最大化
#driver.set_window_size(1920,1080)

driver.get('https://www.baidu.com/')

#在input标签输入内容
driver.find_element_by_id('kw').send_keys('你好')
driver.find_element_by_id('su').click() #点击元素

#页面jieping
#driver.save_screenshot('a.png')

time.sleep(4)
driver.quit() #退出浏览器
