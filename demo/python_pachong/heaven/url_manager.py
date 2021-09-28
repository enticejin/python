'''
URL链接管理类，负责管理爬取下来的电影链接地址，包括新解析出来的链接地址，和已经下载过的链接地址，保证相同的链接地址只会下载一次
'''


class UrlManager(object):
    def __init__(self):
        self.urls = set()
        self.used_urls = set()
        self.download_urls = set()

    def add_url(self, url):
        if url is None:
            return
        if url not in self.urls and url not in self.used_urls:
            self.urls.add(url)

    def add_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_url(url)

    def has_continue(self):
        return len(self.urls) > 0

    def get_url(self):
        url = self.urls.pop()
        self.used_urls.add(url)
        return url

    def get_download_url(self):
        return self.download_urls

    def has_download(self, url):
        return url in self.download_urls

    def add_download_url(self, url):
        if url is None:
            return
        if url not in self.download_urls:
            self.download_urls.add(url)