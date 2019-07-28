import requests, re

class Guoke:
    def __init__(self):
        self.temp_url = 'https://www.guokr.com/ask/highlight/?page={}'

    def parse_url(self,url):
        r = requests.get(url)
        texts = re.findall(r'<h2><a target="_blank" href=".*?">(.*?)</a></h2>',r.text,re.S)
        hrefs = re.findall(r'<h2><a target="_blank" href="(.*?)">.*?</a></h2>',r.text,re.S)
        for text,href in zip(texts,hrefs):
            print(text,href)

    def run(self):
        #1. start_url
        urls = [self.temp_url.format(i) for i in range(1,4)]
        #2. 发送请求，获取响应
        #3. 提取数据
        for url in urls:
            self.parse_url(url)

if __name__ == '__main__':
    guoke = Guoke()
    guoke.run()
