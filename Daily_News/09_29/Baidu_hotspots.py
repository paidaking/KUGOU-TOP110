import requests
from lxml import etree

'''
1.发送请求获取响应内容
2.解析内容获取所需信息
'''

class Baidu_hotspots:
    def __init__(self):
        self.url = 'http://top.baidu.com/buzz?b=1&c=513&fr=topbuzz_b341_c513'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

    def get_url(self):
        try:
            r = requests.get(self.url,headers=self.headers)
            r.encoding = r.apparent_encoding
            content = r.content.decode('gbk')
            #print(content) 检测输出内容正常
            return content
        except:
            return '请求失败'

    def get_content(self,content):
        html = etree.HTML(content)
        title_one = html.xpath('//div[@class="top-title"]/h2/text()')[0] #获取大标题
        print('{:^55}'.format(title_one),'\n')

        #获取排名，关键词，搜索指数三个内容
        nums = html.xpath('//table[@class="list-table"]//td[@class="first"]/span/text()')
        keywords = html.xpath('//table[@class="list-table"]//td[@class="keyword"]/a[1]/text()')
        search_indexs = html.xpath('//table[@class="list-table"]//td[@class="last"]/span/text()')
        #print(nums,keywords,search_indexs)
        for num,keyword,search_index in zip(nums,keywords,search_indexs):
            hotspot = "排名：{0:^4}\t关键词：{1:^15}\t搜索指数：{2:^8}" .format(num,keyword,search_index)
            print(hotspot)

    def main(self):
        content = self.get_url()
        self.get_content(content)

if __name__ == '__main__':
    realtime_hotspot = Baidu_hotspots()
    realtime_hotspot.main()
