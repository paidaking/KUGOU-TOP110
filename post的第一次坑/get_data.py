import requests

cookie = 'SId=pqivjqxyu33xm4dv4bkezpmv; BPRSSP=BPRSSP_pqivjqxyu33xm4dv4bkezpmv'

data = '''{"SId":"BPRSSP_pqivjqxyu33xm4dv4bkezpmv",   #这里的data为啥是str还得研究研究
"startdate":"2019-08-01",
"enddate":"2019-08-21",
"batchNo":"",
"proofTypeName":"0",
"medIds":[],
"supIds":[],
"clientIds":[],
"goodsIds":[],
"orgId":'',
"page":1,
"rows":10,
"sort":"ORG_ID",
"order":"desc"}'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'cookie': cookie
}

res = requests.post('http://bn023.test.s2ps.cn/Sale/GetSaleList', data=data, headers=headers)
print(res.text)
