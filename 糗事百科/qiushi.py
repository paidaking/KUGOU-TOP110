import requests,re

def judge_sex(sex):
    if sex == 'manIcon':
        return '男'
    else:
        return '女'

def get_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
    req = requests.get(url,headers=headers)
    print(req.encoding)
    return req.content.decode()

def parse_page(html):
    titles = re.findall('<h2>(.*?)</h2>',html,re.S)
    ages = re.findall('<div class="articleGender .*?">(.*?)</div>',html,re.S)
    sexs = re.findall('<div class="articleGender (.*?)">.*?</div>',html,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span',html,re.S)
    for title,age,sex,content in zip(titles,ages,sexs,contents):
        data = {
                'title':title.strip(),
                'age':age.strip(),
                'sex':judge_sex(sex.strip()),
                'content':content.strip()
        }
        print(data,'\n')

def main(num):
    url = 'https://www.qiushibaike.com/text/page/' + str(num)
    html = get_page(url)
    parse_page(html)

if __name__ == '__main__':
    for i in range(1,10):
        main(i)
