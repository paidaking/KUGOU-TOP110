import requests, json


class Douban():
    def __init__(self,url):
        self.url = url

    def parse_url(self,url):
        r = requests.get(url)
        html = r.content.decode()
        data = json.loads(html)
        for i in range(20):
            title = data['subjects'][i]['title']
            rate = data['subjects'][i]['rate']
            url = data['subjects'][i]['url']
            print(title,rate,url)

if __name__ == '__main__':
    urls = ['https://movie.douban.com/j/search_subjects?type=tv&tag=%E8%8B%B1%E5%89%A7&sort=recommend&page_limit=20&page_start={}'.format(i*20) for i in range(4)]
    for url in urls:
        douban = Douban(url)
        douban.parse_url(url)
