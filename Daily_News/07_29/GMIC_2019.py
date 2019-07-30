import requests, re
from lxml import etree


class Kunpeng:
    def __init__(self):
        self.url = 'https://tech.sina.com.cn/it/2019-07-27/doc-ihytcitm5053617.shtml'

    def get_url(self):
        r = requests.get(self.url)
        return r.content.decode()

    def parse_url(self,html):
        data = etree.HTML(html)
        title = data.xpath('//h1[@class="main-title"]/text()')[0]
        print(title, '\n')

        ps = data.xpath('//div[@class="article"]/p')
        for p in ps:
            text = p.xpath('./text()')[0].replace('\u3000\u3000', '')
            print(text, '\n')

    def run(self):
        html = self.get_url()
        self.parse_url(html)

if __name__ == '__main__':
    kunpeng = Kunpeng()
    kunpeng.run()
