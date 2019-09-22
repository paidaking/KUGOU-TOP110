import time
import requests
from lxml import etree

class Weather_forecast:

    def getWeather(self):
        # 使用BeautifulSoup获取天气信息
        r=requests.get('https://tianqi.sogou.com/')
        tree=etree.HTML(r.text)
        city=tree.xpath('//em[@class="city-name"]/text()')[0]
        today=tree.xpath('//div[@class="row2 row2-0"]/a/text()')[0].strip()
        weather=tree.xpath('//div[@class="r1-img"]/p/text()')[0]
        wind=tree.xpath('//p[@class="condition"]/span[1]//text()')[1]
        quality=tree.xpath('//span[@class="liv-text"]/a/em/text()')[0]
        rank=tree.xpath('//span[@class="liv-text"]/a/span[2]/text()')[0]
        high=tree.xpath('//div[@class="r-temp"]/@data-high')[0].split(',')[1]
        low=tree.xpath('//div[@class="r-temp"]/@data-low')[0].split(',')[1]
        content='早上好，亲爱的！\n今日份的天气请注意查看喔~\n今天是：'+today+'\n城市：'+city+'\n天气：'+weather+'\n风级：'+wind+'\n最高温度:'+high+'\n最低温度:'+low+'\n空气质量指数:'+quality+' 等级：'+rank
        print(content)
        return content

    def main(self):
        message = self.getWeather()
        print('成功获取天气信息')


if __name__ == '__main__':
    weather = Weather_forecast()
    weather.main()
