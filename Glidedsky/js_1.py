# selenuim破解js反爬虫，没有使用多线程那速度真的是慢的不得了，后续继续更新吧。


from selenium import webdriver
from lxml import etree
import requests

driver = webdriver.Chrome()
driver.get('http://glidedsky.com/login')
input_email = driver.find_element_by_id('email')
input_email.send_keys('******')
input_password = driver.find_element_by_id('password')
input_password.send_keys('******')
input_password = driver.find_element_by_id('password')

submit = driver.find_element_by_xpath('//*[@id="app"]/main/div/div/div/div/div[2]/form/div[4]/div/button')
submit.click()

input_js = driver.find_element_by_xpath('//*[@id="app"]/main/div/div/div/table/tbody/tr[9]/td[1]/a')
input_js.click()

html = etree.HTML(driver.page_source)
target_url = 'http://glidedsky.com' + html.xpath('//*[@id="app"]/main/div/div/div/div/div/a/@href')[0]
print(target_url)

total_urls = [(target_url+ '?page={}').format(i) for i in range(1,1001)]
#print(total_urls)
nums_list = []
for total_url in total_urls:

    driver.get(total_url)
    #print(driver.page_source)
    content = etree.HTML(driver.page_source)
    texts = content.xpath('//div[@class="row"]/div[@class="col-md-1"]/text()')
    #print(texts)
    s = 0
    for text in texts:
        s = int(text.strip()) + s
    print(s)
    nums_list.append(s)
print(nums_list)
nums = 0
for num in nums_list:
    nums = num + nums
print(nums)
