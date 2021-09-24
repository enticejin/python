from urllib import request
from bs4 import BeautifulSoup
import re
import requests
import time


class Music(object):
    def __init__(self, baseurl, path):
        head = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }
        self.baseurl = baseurl
        self.headers = head
        self.path = path

    def main(self):
        html = self.askurl()
        bs4 = self.analysis(html)
        name1 = self.matching(bs4)
        self.save(name1)

    def askurl(self):
        req = request.Request(url=self.baseurl, headers=self.headers)
        response = request.urlopen(req)
        html = response.read().decode("utf-8")
        return html

    def analysis(self, html):
        soup = BeautifulSoup(html, "html.parser")
        bs4 = soup.find_all("textarea")
        bs4 = str(bs4)
        return bs4

    def matching(self, bs4):
        rule0 = re.compile(r'"name":"(.*?)","tns":[],"alias":[]')
        name0 = re.findall(rule0, bs4)
        str = ""
        for i in name0:
            str = str + "," + i
        str = str.replace("\xa0", " ")
        rule1 = re.compile(r'jpg,(.*?),(.*?)","id":(\d*)')
        name1 = re.findall(rule1, str)
        return name1

    def save(self, name1):
        for j in name1:
            print("正在下载：" + j[1] + " - " + j[0] + "...")
            url = "http://music.163.com/song/media/outer/url?id=" + j[2]
            content = requests.get(url=url, headers=self.headers).content
            with open(self.path + j[1] + " - " + j[0] + ".mp3", "wb") as f:
                f.write(content)
            print(j[1] + " - " + j[0] + "下载完毕。\n")
            time.sleep(0.5)
        return


if __name__ == "__main__":
    baseurl = "https://music.163.com/discover/toplist?id=5453912201"  # 要爬取的热歌榜链接
    path = "D:/2345Downloads/cloudmusic/"  # 保存的文件目录
    demo0 = Music(baseurl, path)
    demo0.main()
    print("下载完毕")
