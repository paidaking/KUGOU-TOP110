import requests,csv
from bs4 import BeautifulSoup

def get_page(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
    req = requests.get(url,headers=headers)
    return req.text

def parse_page(html):
    soup = BeautifulSoup(html,'html.parser')
    tops = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num ')
    songs =  soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    times = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    for top,song,time in zip(tops,songs,times):
        data = {
            'top':top.get_text().strip(),
            'song':song.get_text().strip(),
            'lianjie':song.get('href'),
            'time':time.get_text().strip()
        }
        print(data)

def main(num):
    url = 'https://www.kugou.com/yy/rank/home/'+ str(num) +'-8888.html?from=rank'
    html = get_page(url)
    parse_page(html)

if __name__ == '__main__':
    for num in range(1,6):
        main(num)
