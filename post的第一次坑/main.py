import requests, json, csv


def get_checkcode():
    url = 'http://bn023.test.s2ps.cn/checkcode.ashx'
    res = requests.get(url)
    #print(res.status_code)
    #print(res.headers['set-cookie'])
    print(res.headers['set-cookie'][10:-8])  #获取验证码
    checkcode = res.headers['set-cookie'][10:-8]
    return checkcode

def login(checkcode):
    url_login = 'http://bn023.test.s2ps.cn/'

    cookie = 'checkcode=' + checkcode
    data = {
        '__VIEWSTATE': '/wEPDwUJMjgwMjgyODcwZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQULY2hrUmVtZW1iZXKaolWm4uskNdvsiClaAKwnU0QQloh2CFCxKX14zm7HDQ==',
        '__EVENTVALIDATION': '/wEWBgKz8tOiBgLEhISACwKd+7q4BwLR55GJDgLri5LxAgLx29THC8JzNyreoYI35dFtjRLn7wXDNpEXCFE+DThT2oiWiyiM',
        'txtname': 'shkbxy@ldj',
        'txtpwd': 'a1234567',
        'txtcheckcode': checkcode,
        'ImgSubmit': '登录验证中...'
        }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'cookie': cookie
        }

    res_login = requests.post(url_login, data=data, headers=headers)
    #res_login.encoding = res_login.apparent_encoding
    #print(res_login.text)
    #print(res_login.status_code)
    #print(res_login.headers)
    print(res_login.request.headers)
    res_cookie = res_login.request.headers['Cookie']
    #print(res_cookie)
    return res_cookie

def get_data(res_cookie):
    cookie = res_cookie
    sid = cookie.split(';')[-1].split('=')[-1]
    #print(sid)

    data = {
        'SId':sid,
        'startdate':'2019-07-01',
        'enddate':'2019-07-31',
        'batchNo':'',
        'proofTypeName':'0',
        'medIds':[],
        'supIds':[],
        'clientIds':[],
        'goodsIds':[],
        'orgId':'',
        'page':1,
        'rows':10,
        'sort':'ORG_ID',
        'order':'desc'
    }
    data = str(data)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'cookie': cookie
    }
    url = 'http://bn023.test.s2ps.cn/Sale/GetSaleList'
    res = requests.post(url, data=data, headers=headers)
    print(res.text)
    contents = json.loads(res.text)
    contents = contents['retObj']['rows']
    #print(contents)
    datas = []
    for content in contents:
        item = {}
        item['编号'] = content['ROWNO']
        item['出库日期'] = content['DELIVERY_DATE']
        item['销售类型名称'] = content['PROOF_TYPENAME']
        item['商品编码'] = content['GOODS_ID']
        item['商品名称'] = content['GOODS_NAME']
        item['品种规格'] = content['GOODS_SPEC']
        item['批号'] = content['BATCH_NO']
        item['数量'] = content['QUANTITY']
        item['单位'] = content['UNIT_NAME']
        item['价格'] = content['PRICE']
        item['有效期'] = content['VALID_DATE']
        item['客户名称'] = content['CLIENT_NAME']
        item['销售单位名称'] = content['COMPANY_NAME']
        item['合格'] = content['STATUS']
        item['商品通用名'] = content['GOODS_COMNAME']
        item['厂家名称'] = content['MAKERNAME']
        print(item)
        datas.append(item)
    return datas

def save_data(datas):
    with open('医药数据.csv','a',encoding='utf-8') as f:
        fieldnames = ['编号','出库日期','销售类型名称','商品编码','商品名称','品种规格','批号','数量','单位','价格','有效期','客户名称','销售单位名称','合格','商品通用名','厂家名称']
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(datas)

if __name__ == '__main__':
    checkcode = get_checkcode()
    print(checkcode)
    res_cookie = login(checkcode)
    print(res_cookie)
    datas = get_data(res_cookie)
    save_data(datas)
