import urllib

import chardet
import requests
url="https://map.baidu.com/@11876163,3067299,13z"
page =requests.get(url)
encoder = 'utf-8'
try:
    html = urllib.request.urlopen(url).read()
    encoder = chardet.detect(html)['encoding']
except Exception as e:
    print(e)

if encoder == 'utf-8' or encoder == 'UTF-8':
    pass
elif encoder == 'GBK' or encoder == 'gbk':
    page.encoding = 'GBK'
elif encoder == 'GB2312' or encoder == 'gb2312':
    page.encoding = 'GB2312'
else:
    print('请手动查看', page.encoding)

try:
    r=requests.get(url)
    r.raise_for_status()    
    print(r.encoding)
    print(r.text)
except:
    print('爬取信息失败')