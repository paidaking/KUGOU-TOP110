import requests, re
from lxml import etree

class Kunpeng:
    def __init__(self):
        self.url = 'https://www.dramx.com/News/Memory/20190729-17216.html'

    def get_url(self):
        r = requests.get(self.url)
        return r.text

    def parse_url(self,html):
        contents = []
        data = etree.HTML(html)
        title = data.xpath('//div[@class="newspage-header"]/h1/text()')[0][5:]
        texts = data.xpath('//div[@class="newspage-cont"]/p')
        for text in texts[:-2]:
            contents.append(text.text)

        print(title, '\n')

        for content in contents:
            print(content, '\n')

    def run(self):
        html = self.get_url()
        self.parse_url(html)

if __name__ == '__main__':
    kunpeng = Kunpeng()
    kunpeng.run()
