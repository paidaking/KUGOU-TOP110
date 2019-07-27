import requests, json

class Douban:
    def __init__(self):
        self.url_temp = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start={}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36',
                        'Referer': 'https://movie.douban.com/tv/'}

    def parse_url(self,url):
        print(url)
        r = requests.get(url, headers = self.headers)
        json_str = r.content.decode()
        return json_str

    def get_content_list(self, json_str):
        temp_dict = json.loads(json_str)
        return temp_dict['subjects']

    def save_content_list(self, content_list):
        with open('douban.txt', 'a')as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write('\n')
        print('保存成功')

    def run(self):#实现主要逻辑
        num = 0
        while True:
            #1. start_url
            next_url = self.url_temp.format(num)
            #2. 发送请求，获取响应
            json_str = self.parse_url(next_url)
            #3. 提取数据
            content_list = self.get_content_list(json_str)
            #4. 保存
            self.save_content_list(content_list)
            #5. 构造下一页的url地址，循环 2-5步
            num += 20

            if len(content_list)<18:
                break

if __name__ == '__main__':
    douban = Douban()
    douban.run()
