from selenium import webdriver
from PIL import Image, ImageEnhance
import tesserocr
import time


url = 'http://bn023.test.s2ps.cn/'
driver = webdriver.Chrome()
driver.maximize_window()  # 将浏览器最大化
driver.get(url)
time.sleep(1)

# 截取当前网页并命名为printscreen，该网页有我们需要的验证码
driver.save_screenshot('printscreen.png')
imgelement = driver.find_element_by_id('txtcheckcode')  # 定位验证码
location = imgelement.location  # 获取验证码x,y轴坐标
print(location)
size = imgelement.size  # 获取验证码的width,height的坐标
print(size)

# 写成我们需要截取的位置坐标（通过增减确定目标位置，每台电脑的分辨率不一样，请根据自己的电脑找合适的位置）
rangle = (int(location['x']+310), int(location['y']+160), int(location['x'] + size['width']+218),
          int(location['y'] + size['height']+175))  

i = Image.open("printscreen.png")  # 打开截图
frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
frame4=frame4.convert('RGB')
frame4.save('printscreen.jpg') # 保存我们接下来的验证码图片 进行打码

image = Image.open('printscreen.jpg')
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(1)
    else:
        table.append(0)

image = image.point(table, '1')
#image.show()
result = tesserocr.image_to_text(image)
print(result)

time.sleep(2)
driver.close()
