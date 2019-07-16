import requests,re,time
import json

def get_page(num):
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    # 构造请求头
    headers = {
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        'Referer': "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
    }
    form_data = {
        'first': 'true',
        'pn': num,
        'kd': 'python'
    }
    url_start = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
    s = requests.Session()
    s.get(url_start, headers=headers, timeout=3)
    cookie = s.cookies
    response = s.post(url, data=form_data, headers=headers,cookies=cookie, timeout=3)
    return response.json()

def parse_page(job_json):
    results = job_json['content']['positionResult']['result']
    for result in results:
        infos = {
            'companyFullName':result['companyFullName'],
            'city':result['city'],
            'companyLabelList':result['companyLabelList'],
            'companySize':result['companySize'],
            'createTime':result['createTime'],
            'district':result['district'],
            'education':result['education'],
            'financeStage':result['financeStage'],
            'firstType':result['firstType']
        }
        print(infos)

if __name__ == '__main__':
    for page_num in range(1,2):
        job_json = get_page(page_num)
        parse_page(job_json)
        #print('已抓取{}页, 总职位数:{}'.format(page_num, len(all_company)))
        time.sleep(10)
