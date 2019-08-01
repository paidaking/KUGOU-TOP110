import requests
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie': '******'}

def get_page(url):
    r = requests.get(url,headers=headers)
    html = etree.HTML(r.text)
    digits = html.xpath('//*[@class="col-md-1"]/text()')
    s = 0
    for digit in digits:
        i = int(digit.strip())
        s = i + s
    return s

def main():
    urls = ['http://glidedsky.com/level/web/crawler-basic-2?page={}'.format(i) for i in range(1,1001)]
    nums = 0
    for url in urls:
        data = get_page(url)
        nums += data
    print(nums)

if __name__ == '__main__':
    main()
