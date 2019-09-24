import requests,re
from lxml import etree
from fontTools.ttLib import TTFont

class MaoYan:
    def __init__(self):
        self.url = 'https://maoyan.com/films/359377'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

    def get_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response

    def parse_font(self, response):
        font_name = re.search(r"url\('.*?vfile\.meituan\.net\/colorstone\/(\w+\.woff)'\)",response,re.S).group(1)
        #print(font_name)
        font_url = 'https://vfile.meituan.net/colorstone/' + font_name
        font_response = self.get_url(font_url)
        with open(font_name, 'wb') as f:
            f.write(font_response.content)

        basefont = TTFont('basefont.woff')
        basefont.saveXML('basefont.xml')
        basefont_dict = {'uniE46E': '9', 'uniE759': '8', 'uniF175': '6', 'uniE442': '5', 'uniE977': '2',
                         'uniE497': '7', 'uniE966': '1', 'uniF801': '0', 'uniF560': '4', 'uniEDD2': '3'}
        basefont_list = basefont.getGlyphOrder()[2:]
        #print(basefont_list)
        newfont = TTFont(font_name)
        newfont.saveXML('newfont.xml')
        newfont_list = newfont.getGlyphOrder()[2:]
        #print(newfont_list)

        coordinate_list_1 = []
        for base_uni in basefont_list:
            base_coordinate = basefont['glyf'][base_uni].coordinates
            coordinate_list_1.append(base_coordinate)
        #print(coordinate_list_1)

        coordinate_list_2 = []
        for new_uni in newfont_list:
            new_coordinate = newfont['glyf'][new_uni].coordinates
            coordinate_list_2.append(new_coordinate)
        #print(coordinate_list_2)

        index_2 = -1
        newfont_dict = {}
        for name2 in coordinate_list_2:
            index_2 += 1
            index_1 = -1
            for name1 in coordinate_list_1:
                index_1 += 1
                if self.compare(name1,name2):
                    newfont_dict[newfont_list[index_2]] = basefont_dict[basefont_list[index_1]]

        for i in newfont_dict:
            pattern = i.replace('uni','&#x').lower() + ';'
            response = response.replace(pattern, newfont_dict[i])
        return response

    def compare(self,c1,c2):
        for i in range(7):
            if abs(c1[i][0] - c2[i][0]) < 70 and abs(c1[i][1]-c2[i][1]) < 70:
                pass
            else:
                return False
        return True


    def parse_url(self, response):
        html = etree.HTML(response)
        item = {}
        item['movie_name'] = html.xpath('//div[@class="celeInfo-right clearfix"]/div[1]/h3/text()')[0]
        item['start_time'] = html.xpath('//div[@class="celeInfo-right clearfix"]/div[1]/ul/li[3]/text()')[0]
        item['用户评分'] = html.xpath('//div[@class="celeInfo-right clearfix"]/div[3]/div[1]/div/span/span/text()')[0]
        item['评分人数'] = html.xpath('//div[@class="celeInfo-right clearfix"]/div[3]/div[1]/div/div/span/span/text()')[0] + html.xpath(
            '//div[@class="celeInfo-right clearfix"]/div[3]/div[1]/div/div/span/span/following-sibling::text()')[0]
        item['累计票房'] = html.xpath('//div[@class="celeInfo-right clearfix"]/div[3]/div[2]/div/span[1]/text()')[0] + html.xpath(
            '//div[@class="celeInfo-right clearfix"]/div[3]/div[2]/div/span[2]/text()')[0]
        print(item)

    def main(self):
        response = self.get_url(self.url).text
        response = self.parse_font(response)
        self.parse_url(response)

if __name__ == '__main__':
    maoyan = MaoYan()
    maoyan.main()
