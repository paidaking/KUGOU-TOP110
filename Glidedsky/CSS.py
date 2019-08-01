import requests, re, time
from lxml import etree

class Spider_CSS:
    def __init__(self):
        self.url = 'http://glidedsky.com/level/web/crawler-css-puzzle-1?page={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                        'Cookie': '_ga=GA1.2.186470669.1563545221; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1563545221,1564666541; _gid=GA1.2.1802999429.1564666541; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImpGeWxrUUd6S2xIM1RFK292Y1RJOWc9PSIsInZhbHVlIjoiaEptajJTR1grdXQydHlnY3krRDNDdFZZQWpGOVk0N25TbTh5UEJBdEdMdWtcL25YYnB3a0Y5bmRwSktXTDc0TlNva2ZGMlwvWEVlQVQwa2tqTVIwc0U2NDZCXC9pUUhVZWFOckJ2VlhCcHhLK1UyXC9jWlhIaCsxXC9mdEprdkFxK2d0eWdDRUNyTTRqekFPbHJWblN4ZGRNdVkxT3ZkRUhHa2tTT2R2Z3k5Q2tteEU9IiwibWFjIjoiNmVhYjg0ZTc2MWI0YWEwMzhkNTRjODY2ZWI4MWIwYjlkYWY5YTVlNzMzMjQ4MmEwNDE4MWIwMzZkNTg4NWRkNiJ9; XSRF-TOKEN=eyJpdiI6InBPNG5lQUNoM0ZFNlp3eWVtRnRIOUE9PSIsInZhbHVlIjoiXC83anYrZ1wvS0V2UDBzXC9WeVdUeGRcL3N3TThQVFF4MTRvTytkWkpcL3RVaFBaeDhVcjliRHdoZnVPMGFnNkIwSCtBIiwibWFjIjoiODE1YmViZmVkMGY3OWI0M2EyYjkxYmEwMDU3ZDk2NTIwOWRmZWU5YjUwYzI5MGVhMDY5NDBjOWEzOGVlOTg5MSJ9; glidedsky_session=eyJpdiI6IkFlWGM2VEJhTkJDdjBqUkE1TjlFU3c9PSIsInZhbHVlIjoiXC8rbmV0YXdXN3pIdUY5Q0JRRXVXczRhdWhybXQra0ZLZ0t4SGxpOVM1Y1l3b0hqWnJ5WWVUakYrM1NDTkc3MkwiLCJtYWMiOiIzYzk1ZjVjYzEwMjg0NTI4ZDI2NmViMDllNDllYzc0YTAyM2JiMTQ4ZjFjZGYyZTU4NDg0MzhlNDg4YmUwNWU2In0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1564669490; _gat_gtag_UA_75859356_3=1'
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
