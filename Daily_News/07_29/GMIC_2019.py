import requests, re
from lxml import etree

class Kunpeng:
    def __init__(self):
        self.url = 'https://tech.sina.com.cn/it/2019-07-27/doc-ihytcitm5053617.shtml'

    def get_url(self):
        r = requests.get(self.url)
        return r.content.decode()

    def parse_url(self,html):
        contents = []
        data = etree.HTML(html)
        title = data.xpath('//h1[@class="main-title"]/text()')[0]
        texts = data.xpath('//div[@class="article"]/p')
        for text in texts:
            contents.append(text.text)

        print(title, '\n')

        for content in contents[:-1]:
            print(content.strip(), '\n')

    def run(self):
        html = self.get_url()
        self.parse_url(html)

if __name__ == '__main__':
    kunpeng = Kunpeng()
    kunpeng.run()
