import requests, re
from lxml import etree

class Kunpeng:
    def __init__(self):
        self.url = 'http://baijiahao.baidu.com/s?id=1640441990442745885&wfr=spider&for=pc'

    def get_url(self):
        r = requests.get(self.url)
        return r.content.decode()

    def parse_url(self,html):
        data = etree.HTML(html)
        title = data.xpath('//div[@class="article-title"]/h2/text()')[0]
        print(title, '\n')

        ps = data.xpath('//div[@class="article-content"]/p')
        for p in ps:
            text = p.xpath('./span//text()')[0]
            print(text, '\n')

    def run(self):
        html = self.get_url()
        self.parse_url(html)

if __name__ == '__main__':
    kunpeng = Kunpeng()
    kunpeng.run()

