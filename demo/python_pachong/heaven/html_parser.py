from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import urllib.parse
import base64

'''
html页面解析器
'''


class HtmlParser(object):
    # 解析电影列表页面，获取电影详情页面的链接
    def parser_movie_link(self, content):
        try:
            urls = set()
            next_link = None
            doc = BeautifulSoup(content, 'lxml')
            div_content = doc.find('div', class_='co_content8')
            if div_content is not None:
                tables = div_content.find_all('table')
                if tables is not None and len(tables) > 0:
                    for table in tables:
                        link = table.find('a', class_='ulink')
                        if link is not None:
                            print('movie name: ' + link.text)
                            movie_link = urljoin('https://www.dytt8.net', link.get('href'))
                            print('movie link ' + movie_link)
                            urls.add(movie_link)
                next = div_content.find('a', text=re.compile(r".*?下一页.*?"))
                if next is not None:
                    next_link = urljoin('https://www.dytt8.net/html/gndy/dyzz/', next.get('href'))
                    print('movie next link ' + next_link)

            return urls, next_link
        except Exception as e:
            print('解析电影链接地址发生错误: ' + str(e))

    # 解析电影详情页面，获取电影详细信息
    def parser_movie_info(self, content, score=8):
        try:
            movie_name = None  # 电影名称
            movie_score = 0  # 电影评分
            movie_xunlei_links = set()  # 电影的迅雷下载地址，可能存在多个
            doc = BeautifulSoup(content, 'lxml')
            movie_name = doc.find('title').text.replace('迅雷下载_电影天堂', '')
            # print(movie_name)
            div_zoom = doc.find('div', id='Zoom')
            if div_zoom is not None:
                # 获取电影评分
                span_txt = div_zoom.text
                txt_list = span_txt.split('◎')
                if txt_list is not None and len(txt_list) > 0:
                    for tl in txt_list:
                        if 'IMDB' in tl or 'IMDb' in tl or 'imdb' in tl or 'IMdb' in tl:
                            txt_score = tl.split('/')[0]
                            print(txt_score)
                            movie_score = re.findall(r"\d+\.?\d*", txt_score)
                            if movie_score is None or len(movie_score) <= 0:
                                movie_score = 1
                            else:
                                movie_score = movie_score[0]
                print(movie_name + ' IMDB影片分数: ' + str(movie_score))
                if float(movie_score) < score:
                    print('电影评分低于' + str(score) + ', 忽略')
                    return movie_name, movie_score, movie_xunlei_links
                txt_a = div_zoom.find_all('a', href=re.compile(r".*?ftp:.*?"))
                if txt_a is not None:
                    # 获取电影迅雷下载地址，base64转成迅雷格式
                    for alink in txt_a:
                        xunlei_link = alink.get('href')

                        #这里将电影链接转换成迅雷的专用下载链接，后来发现不转换迅雷也能识别
                        xunlei_link = urllib.parse.quote(xunlei_link)
                        xunlei_link = xunlei_link.replace('%3A', ':')
                        xunlei_link = xunlei_link.replace('%40', '@')
                        xunlei_link = xunlei_link.replace('%5B', '[')
                        xunlei_link = xunlei_link.replace('%5D', ']')
                        xunlei_link = 'AA' + xunlei_link + 'ZZ'
                        xunlei_link = base64.b64encode(xunlei_link.encode('gbk'))
                        xunlei_link = 'thunder://' + str(xunlei_link, encoding='gbk')

                        print(xunlei_link)
                        movie_xunlei_links.add(xunlei_link)
            return movie_name, movie_score, movie_xunlei_links
        except Exception as e:
            print('解析电影详情页面错误: ' + str(e))



