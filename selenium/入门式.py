# 入门式

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
print(driver.page_source)


# 关闭页面

driver.close() : 关闭当前页面
driver.qiut(): 退出整个浏览器

# 定位元素

使用By就必须导入；
from selenium.webdriver.common.by import By

find_element_by_id : 根据id来查找某个元素。等价于：
submitTag = driver.find_element_by_id('su')
submitTag = driver.find_element(By_ID,'su')

find_element_by_class_name : 根据类名查找元素。等价于：
submitTag = driver.find_element_by_class_name('su')
submitTag = driver.find_element(By.CLASS_NAME,'su')

find_element_by_name : 根据name属性的值来查找元素。等价于：
submitTag = driver.find_element_by_name('email')
submitTag = driver.find_element(By.NAME,'email')

find_element_by_tag_name : 根据标签名来查找元素。等价于：
submitTag = driver.find_element_by_tag_name('div')
submitTag = driver.find_element(By.TAG_NAME,'div')

find_element_by_xpath : 根据xpath语法来查找元素。等价于：
submitTag = driver.find_element_by_xpath('//div')
submitTag = driver.find_element(By.XPATH,'//div')

find_element_by_selector : 根据css选择器选择元素。等价于：
submitTag = driver.find_element_by_css_selector('')
submitTag = driver.find_element(By.CSS_SELECTOR,'')

# find_elements 表示获取全部

send_keys('') # 输入关键字
click() # 点击
clear() # 清除

# 操作表单元素

# 行为链

input = driver.find_element_by_id('kw')
submit = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(input)
actions.send_keys_to_element(input,'python')
actions.move_to_element(submit)
actions.perform()

click_and_hold(element):点击但不松开鼠标
content_click(element):右键点击
double_click(element):双击

#——————————————————————————————————————————————————

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
input1.send_keys('******')

# 定位并输入密码
input2 = driver.find_element_by_name('password')
input2.send_keys('******')

# 定位并点击【下次自动登录】
remember_botton = driver.find_element_by_id('account-form-remember')
remember_botton.click()

# 登陆
login_botton = driver.find_element_by_xpath('//a[contains(@class,"btn-account")]')
login_botton.click()

