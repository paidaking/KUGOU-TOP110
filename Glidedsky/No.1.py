import requests
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie': 'Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1563508515; _ga=GA1.2.110110218.1563508515; _gid=GA1.2.1968679634.1563508515; _gat_gtag_UA_75859356_3=1; XSRF-TOKEN=eyJpdiI6Ikp4UHo4SXg3T3RSek05SStpTXA0ZEE9PSIsInZhbHVlIjoiV0c2Qm1Vekp5RVRRTElWZ3hEV1hiU2lcLzhyN3Jidzd0cmFEOWc2eElRVndkNG5HVDlCSjJ3dzdOWEs0YlNrbkgiLCJtYWMiOiI4OTNkNzdmN2Y4ZTExOWIxMmVjZmNlMjUzNzA0N2JkNTNiMDFkYjFkODQ5ODFlNTBjNzg5YTg1MGYzYWE2ZmFlIn0%3D; glidedsky_session=eyJpdiI6IkZYRVNsV25MMnowYlZIN2VERWFkakE9PSIsInZhbHVlIjoiektnZzRzSHBXV2ZjT0RnQ1g3dk54NmxqeVhVVllNcUFmUmk5WnRrWkY4OFZ6em9YbU5iVkZsQllZYkZFN041diIsIm1hYyI6IjJkM2U1Mzc2OTE5MzFhNzM3NmZiMmI4ZTUxMTUyYjEzM2MwNjQ1NTcwNTUzOThmYTNlMDA3Y2EwNGFjNDA1YmUifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1563509972'
}

def get_page(url):
    r = requests.get(url,headers=headers)
    html = etree.HTML(r.text)
    digits = html.xpath('//*[@class="col-md-1"]/text()')
    s = 0
    for digit in digits:
        i = int(digit.strip())
        s = i + s
    return s

def main():
    url = 'http://glidedsky.com/level/web/crawler-basic-1'
    data = get_page(url)
    print(data)

if __name__ == '__main__':
    main()
