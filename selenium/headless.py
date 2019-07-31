from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 创建chrome参数对象,设置chrome浏览器无界面模式
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 创建chrome无界面对象
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://baidu.com/')
print(browser.page_source)
