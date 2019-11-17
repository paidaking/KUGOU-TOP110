import base64, requests
from fontTools.ttLib import TTFont, BytesIO
from bs4 import BeautifulSoup

headers = {'ser-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
           'Cookie':'_ga=GA1.2.605153304.1573659109; footprints=eyJpdiI6IlM0SGU4M1pRTENcL2hTY3N5K0hza2dBPT0iLCJ2YWx1ZSI6IjFHYjE5QzBRTExZdDVnQTZWMDdEc014ZHFoalg0Z0hBTVB4emNPTlF2QXJyTkpGOWxrS3JhVmlwbGVKV29LMGciLCJtYWMiOiIyOGU5ZjY3ZWRhZDUzYTM1ZDQ0ZGVhYzdmOGI0NDQyNmUwMzE1YmRmMDhmYTQ5OTA4YWQ3NWE3YmI3NmE3ZWM4In0%3D; _gid=GA1.2.2110447211.1573900634; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImFKWk9EUWt4d0FXdDVWK2ExeUllRVE9PSIsInZhbHVlIjoiRmozMng1Q0FsMUNxNk5EZzc2NnZZSlpVNWVuVk5TR05heTVEZm5kZU0xaXpzME9WSEQ5d0VheE1VbFczZjdsV1JuREVWeGpJK1wvXC9mSW1CeVdUSEs4Y0lraHB6ZVUxSzBZcHZTR0lZdWd0QVYrbVc2ZXU1TmJHZXRkaSszYm9adXRzS0F2S0VFclA0eTlBVFc1SmdJS1lCTGNoSStHSThtYmlrSTgxOHgrcEk9IiwibWFjIjoiOTcyOGM5NTk0NGI5NTVmMzRiNTUxYWZlOWIyYzg1NWU5NTBmYjc5NTI0MWZlYmI5ZGQ3ZDc0NDIxZDkyMjY0YyJ9; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1573733527,1573900634,1573901319,1573979042; XSRF-TOKEN=eyJpdiI6ImVMQ3JRUjM0QXhoU3lYRW9kXC95WSt3PT0iLCJ2YWx1ZSI6IjZkYnZjZG10eStRSEpaTm5Jb0NRVGpQVkVHYnVINmxzSG5GNVBIbHpxR2NpZEoydnU0eTMreGRnNlJQYWdWWjEiLCJtYWMiOiIzMmUzZGZjNWYzNTFlMzI4MDY5YjQ3YTc0OGFjOWUxNjMwOGNjMjNmZTA1YjA3NTlhM2ZiNGQ3OGIyYmUyZThmIn0%3D; glidedsky_session=eyJpdiI6IndaTVo1azFreWIxUjR4a2dDeXhWWlE9PSIsInZhbHVlIjoiMkxNMVwvUTMxUkhzQ0VyWURCV2dBaWJBY0JBYzN6T0JIbWp2QU9tVmh1U0d6c2RVR3Jaa1htUGdcLzVLQ2tsM1dpIiwibWFjIjoiMzdiNmY4NWE2MmNhY2U0ZDVjZDFlN2E4ZmJhZjNjZTBjYzI2ZWZlNDIxYTAyZDgwNzhjZjlmNDMwZWNiNmE2MSJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1574001640; _gat_gtag_UA_75859356_3=1'
           }

def make_font_file(base64_string):
    bin_data = base64.decodebytes(base64_string.encode())
    with open('online.ttf', "wb") as f:
        f.write(bin_data)
    return bin_data

def convert_font_num(nums):
    base_cid = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}  # 通过xml文件分析得到此结果
    online_font = TTFont('online.ttf').getGlyphOrder()[1:]  # 获取GlyphOrder字段，经对比xml查看此字段是变化的，并且变化的映射关系(cmap)对应真实数字，cmap项不变化, glfy项变化
    real_num_list = []  # 保存替换后的数字
    for n in nums:
        base_cid_key = list(base_cid.keys())[list(base_cid.values()).index(n)]  # 根据字典value获取key值
        online_font_index = online_font.index(base_cid_key)  # 获取列表中对应值的下标
        real_num_list.append(str(online_font_index))
    real_num = ''.join(real_num_list)  # 组合替换后的每一个数字子
    return real_num

urls = ['http://glidedsky.com/level/web/crawler-font-puzzle-1?page={}'.format(i) for i in range(1,1001)]
datas = []
for url in urls:
    r = requests.get(url, headers=headers)
    # print(r.text)

    soup = BeautifulSoup(r.text, "lxml")
    font_style = soup.select_one("style")   
    font_style = font_style.get_text()
    font_style_bs64 = font_style.split(',')[1].split(')')[0]
    #print(font_style_bs64)

    make_font_file(font_style_bs64)
    select = soup.select("div.col-md-1")    
    all_num = []
    s = 0
    for i in select:
        num = i.get_text().strip()
        num = convert_font_num(num)
        all_num.append(int(num))
    for data in all_num:
        s = data + s
    print(s)
    datas.append(s)
#print(datas)
contents = 0
for content in datas:
    contents = content + contents
print(contents)
