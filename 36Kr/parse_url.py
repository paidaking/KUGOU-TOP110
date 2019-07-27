import requests, json, re

#1.url
#2.发送请求，获取响应
#3.提取数据
#4.保存

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

def parse_url(url):
    r = requests.get(url, headers=headers)
    html_str = re.findall('<script>window.initialState=(.*?)</script>', r.content.decode(),re.S)[0]
    print(json.loads(html_str))

def main():
    url = 'https://36kr.com/'
    parse_url(url)

if __name__ == '__main__':
    main()
