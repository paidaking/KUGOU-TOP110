import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

def get_page(url):
    req = requests.get(url,headers=headers)
    req.encoding = req.apparent_encoding
    return req.text

def parse_page(html):
    soup = BeautifulSoup(html,'html.parser')
    title = soup.select('body > div.main > div.entry-tit > h1')
    text = soup.select('body > div.main > div.entry-text > div.m-post')
    tits = title[0].get_text().strip()
    txts = text[0].get_text().strip()
    print(tits,'\n',txts,'\n')

def main():
    for i in range(1,20):
        url = 'http://www.doupoxs.com/doupocangqiong/' + str(i) + '.html'
        html = get_page(url)
        parse_page(html)

if __name__ == '__main__':
    main()
