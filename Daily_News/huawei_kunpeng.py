import requests, re
from lxml import etree

class Kunpeng:
    def __init__(self):
        self.url = 'https://tech.163.com/19/0729/07/EL83M3VO00097U7S.html'

    def get_url(self):
        r = requests.get(self.url)
        return r.text

    def parse_url(self,html):
        data = etree.HTML(html)
        title = data.xpath('//*[@id="epContentLeft"]/h1/text()')[0].strip()
        source_1 = data.xpath('//*[@id="ne_article_source"]/text()')[0]
        source_2 = data.xpath('//*[@id="ne_article_source"]/previous_sibling::text()')[0]
        source = source_1 + source_2
        text_1 = data.xpath('//*[@id="endText"]/p[5]/text()')[0].strip()
        text_2 = data.xpath('//*[@id="endText"]/p[6]/text()')[0].strip()
        print(title, '\n', source, '\n', text_1, '\n', text_2)

    def run(self):
        html = self.get_url()
        self.parse_url(html)

if __name__ == '__main__':
    kunpeng = Kunpeng()
    kunpeng.run()
