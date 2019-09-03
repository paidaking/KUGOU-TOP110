import requests, re, time
from lxml import etree

class Spider_CSS:
    def __init__(self):
        self.url = 'http://glidedsky.com/level/web/crawler-css-puzzle-1?page={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                        'Cookie': '******'
                        }
        self.totle_num = 0

    def get_str(self, url):
        r = requests.get(url, headers=self.headers)
        content_str = r.content.decode()
        return content_str


    def parse_content_str(self, content_str):
        html = etree.HTML(content_str)
        divs_list = html.xpath('//div[@class="col-md-1"]')
        return divs_list


    def parse_divs_list(self, divs_list, content_str):
        for divs in divs_list:
            div_list = divs.xpath('./div')

            if len(div_list) < 3:
                for div in div_list:
                    text = div.xpath("./text()")
                    if not text:
                        class_name = div.xpath("./@class")[0]
                        num1 = re.findall(r"\.{}\:before\s*.*?\s*content\:\"(\d*)\"".format(class_name), content_str, re.S)[0]
                        print(num1)
                        self.totle_num += int(num1)
                        print('总数', self.totle_num)

            else:
                if len(div_list) == 4:
                     div_list = div_list[1:]
                number = [-1, -1, -1]
                for i in range(0, len(div_list)):
                    div = div_list[i]
                    class_name = div.xpath("./@class")[0]
                    data = div.xpath("./text()")[0]
                    left = re.findall(r"\.{}\s.*?\sleft\:(.*?)em".format(class_name), content_str)
                    if not left:
                        number[i] = data

                    else:
                        index = i + int(left[0])
                        number[index] = data
                num2 = "".join(number)
                print(num2)
                self.totle_num += int(num2)
                print('总数', self.totle_num)


    def run(self):
        num = 1
        while True:
            next_url = self.url.format(num)
            content_str = self.get_str(next_url)
            divs_list = self.parse_content_str(content_str)
            self.parse_divs_list(divs_list,content_str)
            print('第 {} 页采集完成'.format(num))
            time.sleep(0.3)
            num += 1

            if len(divs_list)<12:
                break

if __name__ == '__main__':
    kunpeng = Spider_CSS()
    kunpeng.run()
