from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.douban.com/')

# 找到登陆框架
iframe = driver.find_element_by_tag_name('iframe')
# 跳转到登陆框架
iframe = driver.switch_to.frame(iframe)

# 定位并点击【密码登陆】
pw_botton = driver.find_element_by_xpath('//li[contains(@class,"account-tab-account")]')
pw_botton.click()

# 定位并输入用户名
input1 = driver.find_element_by_name('username')
input1.send_keys('18352386687')

# 定位并输入密码
input2 = driver.find_element_by_name('password')
input2.send_keys('wj020700')

# 定位并点击【下次自动登录】
remember_botton = driver.find_element_by_id('account-form-remember')
remember_botton.click()

# 登陆
login_botton = driver.find_element_by_xpath('//a[contains(@class,"btn-account")]')
login_botton.click()

