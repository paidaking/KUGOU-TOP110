import requests
from lxml import etree

count = 1

def get_url(url):
	global count
	req = requests.get(url)
	html = etree.HTML(req.text)
	datas = html.xpath('//*[@id="j-catalogWrap"]/div[2]/div[1]/ul/li/a')
	for data in datas:
		if count<11:
			chapter = data.text
			print(chapter,'\n')
			href = data.get('href')
			href = 'https:' + href
			parse_url(href)
			count += 1

def parse_url(href):
	req = requests.get(href)
	html = etree.HTML(req.text)
	contents = html.xpath('//*[@class="main-text-wrap"]/div[2]/p/text()')
	for content in contents:
		print(content.strip())
	print('\n')

if __name__ == '__main__':
	url = 'https://book.qidian.com/info/1005829524'
	get_url(url)
