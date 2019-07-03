import requests,xlwt
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

def parse_page(url,infos):
    req = requests.get(url,headers=headers)
    selector = etree.HTML(req.text)
    texts = selector.xpath('//div[@class="book-mid-info"]')
    infos=[]
    for text in texts:
        title = text.xpath('h4/a/text()')[0]
        url = text.xpath('h4/a/@href')[0].replace('//','')
        author = text.xpath('p[1]/a[1]/text()')[0]
        type1 = text.xpath('p[1]/a[2]/text()')[0]
        type2 = text.xpath('p[1]/i/text()')[0]
        type3 = text.xpath('p[1]/a[3]/text()')[0]
        type = type1 + type2 + type3
        state = text.xpath('p[1]/span/text()')[0]
        abstract = text.xpath('p[2]/text()')[0].strip()
#        word = text.xpath('p[3]/span/span/text()')[0]
        info = [title,url,author,type,state,abstract]
#        print(info)
        infos.append(info)
    return infos

def save_file(infos):
    header = ['title','url','author','type','state','abstract']
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet1')
    for h in range(len(header)):
        sheet.write(0,h,header[h])
    i=1
    for info in infos:
        j=0
        for data in info:
            sheet.write(i,j,data)
            j+=1
        i+=1
    book.save('起点小说.xls')

def main(num):
    infos=[]
    url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=' + str(num)
    data = parse_page(url,infos)
    print(data)
    save_file(data)

if __name__ == '__main__':
    for i in range(1,6):
        main(i)
