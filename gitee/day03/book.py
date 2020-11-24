# 导入 requests 库
import requests
# 导入文件操作库
import codecs
from bs4 import BeautifulSoup
import sys
import importlib

# 给请求指定一个请求头来模拟Chrome浏览器
global headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
server = 'http://www.tianxiabachang.cn'
# 星辰变地址
book = 'http://www.tianxiabachang.cn/5_5731/'
# 定义一个存储位置,在D盘新建一个文件夹名为星辰变
global save_path
save_path = 'D:/星辰变'


# 获取章节内容
def get_contents(chapter):
    req = requests.get(url=chapter)
    html = req.content
    html_doc = str(html, 'UTF-8')
    bf = BeautifulSoup(html_doc, 'html.parser')
    texts = bf.find_all('div', id='content')
    # 获取div标签id属性content的内容 \xa0 是不间断空白符 &nbsp;
    content = texts[0].text.replace('\xa0' * 4, '\n')
    return content


# 写入文件
def write_txt(chapter, content, code):
    with codecs.open(chapter, 'a', encoding=code) as f:
        f.write(content)


# 主方法
def main():
    res = requests.get(book, headers=headers)
    html = res.content
    html_doc = str(html, 'UTF-8')
    # 使用当前自带的html.parser解析
    soup = BeautifulSoup(html_doc, 'html.parser')
    # 获取所有章节
    a = soup.find('div', id='list').find_all('a')
    print('总章节数： %d' % len(a))
    for each in a:
        try:
            chapter = server + each.get('href')
            content = get_contents(chapter)
            chapter = save_path + "/" + each.string + ".txt"
            write_txt(chapter, content, 'utf8')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
