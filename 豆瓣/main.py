import requests,csv
from lxml import etree

def parse_page(url,content):
    content = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
    req = requests.get(url,headers=headers)
    text = etree.HTML(req.text)
    items = text.xpath('//tr[@class="item"]')
    for item in items:
        title = item.xpath('td[2]/div[1]/a/text()')[0].strip()
        url = item.xpath('td[2]/div[1]/a/@href')[0]
        book_items = item.xpath('td[2]/p[1]/text()')[0]
        author = book_items.split('/')[0]
        publisher = book_items.split('/')[-3]
        time = book_items.split('/')[-2]
        price = book_items.split('/')[-1]
        rate = item.xpath('td[2]/div[2]/span[2]/text()')[0]
        comment = item.xpath('td[2]/p[2]/span/text()')
        data = {
                'title':title,
                'url':url,
                'author':author,
                'publisher':publisher,
                'time':time,
                'price':price,
                'rate':rate,
                'comment':comment
        }
        content.append(data)
    return content

def save_file(content):
    with open('豆瓣图书_Top_250.csv','a',encoding='utf-8') as f:
        fieldnames = ['title','url','author','publisher','time','price','rate','comment']
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(content)

def main(num):
    content={}
    url = 'https://book.douban.com/top250?start=' + str(num)
    info = parse_page(url,content)
    save_file(info)

if __name__ == '__main__':
    for i in range(10):
        print('\n','输出第{}页内容信息:'.format(i+1),'\n')
        main(i*25)
