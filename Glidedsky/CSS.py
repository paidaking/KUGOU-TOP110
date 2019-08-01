import requests, re
from lxml import etree

class Spider_CSS:
    def __init__(self):
        self.url = 'http://glidedsky.com/level/web/crawler-css-puzzle-1?page=1'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                        'Cookie': '_ga=GA1.2.110110218.1563508515; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6InBJVmcraGtSYWR6emxHWU94YU13SFE9PSIsInZhbHVlIjoiYUdrcE9CNUdkbFY0UXRHSVpMbTI2RDBGSlB4bCtIVzhXWjlqMzV2ekNMMmRFRWtqaHJFQVlvSjRtaUJZRVFKYWRSSU03TjNcL1NcL2dvSVFHSFJrc2ZHQVVGNkIyM09aVkdNbU1cL21DVUY2d1RPNTBVUlwvQzM0RVliQlZUcHZtK1ZXMXI3aTFzM2hUdE4zbDBUSWhHV1NObG5cL0paUHdpbEJ0TEpvMHcwYzJNSHc9IiwibWFjIjoiNmM4MjhkZjBlYTFhNTg1OTljNWUwNzUwMTdlOWU4NjBjZmMyOTNjMTU1NDJhYmYzMDk1N2YwMTgzNGYwNmM3MSJ9; _gid=GA1.2.1033840215.1564552863; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1563513314,1563515302,1564552862,1564635332; XSRF-TOKEN=eyJpdiI6Im14bHR1dFwvQ29lZ2ZqYnFPTjJvdGhBPT0iLCJ2YWx1ZSI6IlB3aCt1TFlsVmV0VThtelphdEJlRzB3djQxVXRDckJHMkVPcXpUS2NaMnM4NnJINkZlUFVwbFdTVDRkTTE1MloiLCJtYWMiOiJkYzY4MmRhZTk2YTJmYWY0NmYwOWZjMjBhNGZiYTIxZDI3MjhmN2ExZWZiMTMwZDNkNzMzMjM4YjZjZThhN2JhIn0%3D; glidedsky_session=eyJpdiI6InNEN0xTM1djOEF1UE1BZlhkNHBLTEE9PSIsInZhbHVlIjoiZnRrZExiSW0xdHBaNE9cL3dqa2RWbGduRjBHKzU2VjZTdlJqMnN2RkcxeVpQc3Q4Q092QThvZ2JCSjZITThxNUUiLCJtYWMiOiIxZGEwMTcxNWVkNThhNzllNjRiMmY1ZWU3ZmJhNTgzZjkzNWMzYjFkMThmOTcxOWQxN2U2MTkzYjcwZDlmM2EzIn0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1564637547'
        }

    def get_urls(self):
        pass

    def get_str(self):
        r = requests.get(self.url, headers=self.headers)
        content_str = r.content.decode()
        return content_str

    def parse_content_str(self,content_str):
        html = etree.HTML(content_str)
        divs_list = html.xpath('//div[@class="col-md-1"]')
        return divs_list

    def parse_divs_list(self,divs_list,content_str):
        for divs in divs_list:
            div_list = divs.xpath('./div')

            if len(div_list) < 3:
                for div in div_list:
                    text = div.xpath("./text()")
                    if not text:
                        class_name = div.xpath("./@class")[0]
                        num = re.findall(r"\.{}\:before\s*.*?\s*content\:\"(\d*)\"".format(class_name), content_str, re.S)[0]
                        print(num)
                        

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
                num = "".join(number)
                print(num)
               

    def run(self):
        content_str = self.get_str()
        divs_list = self.parse_content_str(content_str)
        self.parse_divs_list(divs_list,content_str)

if __name__ == '__main__':
    kunpeng = Spider_CSS()
    kunpeng.run()
