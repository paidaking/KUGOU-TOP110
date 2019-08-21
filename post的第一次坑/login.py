import requests
import pytesseract
from PIL import Image

url = 'http://bn023.test.s2ps.cn/checkcode.ashx'
res = requests.get(url)

print(res.status_code)
#print(res.headers['set-cookie'])
print(res.headers['set-cookie'][10:-8])
checkcode = res.headers['set-cookie'][10:-8]

'''
with open('D://111.jpg', 'wb') as f:
    f.write(res.content)

image = Image.open('D://111.jpg')
image = image.convert('RGB')
image = image.convert('L')
threshold = 222
table = []
for i in range(256):
    if i < threshold:
        table.append(1)
    else:
        table.append(0)
image = image.point(table, '1')
image = image.convert('L')
#image.show()
print(pytesseract.image_to_string(image))
'''

cookie1 = 'checkcode=' + checkcode
data1 = {
    '__VIEWSTATE': '/wEPDwUJMjgwMjgyODcwZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQULY2hrUmVtZW1iZXKaolWm4uskNdvsiClaAKwnU0QQloh2CFCxKX14zm7HDQ==',
    '__EVENTVALIDATION': '/wEWBgKz8tOiBgLEhISACwKd+7q4BwLR55GJDgLri5LxAgLx29THC8JzNyreoYI35dFtjRLn7wXDNpEXCFE+DThT2oiWiyiM',
    'txtname': 'shkbxy@ldj',
    'txtpwd': 'a1234567',
    'txtcheckcode': checkcode,
    'ImgSubmit': '登录验证中...'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'cookie': cookie1
}

url_login = 'http://bn023.test.s2ps.cn/'

res_login = requests.post(url_login, data=data, headers=headers)
print(res_login.headers)
print(res_login.request.headers)
print(res_login.status_code)
