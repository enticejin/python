import requests
from requests import Timeout

'''
HtmlDownload，通过一个链接地址将该html页面整体down下来，然后通过html_parser.py解析其中有价值的信息
'''


class HtmlDownload(object):
    def __init__(self):
        self.request_session = requests.session()
        self.request_session.proxies

    def down_html(self, url, retry_count=3, headers=None, proxies=None, data=None):
        if headers:
            self.request_session.headers.update(headers)
        try:
            if data:
                content = self.request_session.post(url, data=data, proxies=proxies)
                print('result code: ' + str(content.status_code) + ', link: ' + url)
                if content.status_code == 200:
                    return content.content
            else:
                content = self.request_session.get(url, proxies=proxies)
                print('result code: ' + str(content.status_code) + ', link: ' + url)
                if content.status_code == 200:
                    return content.content
        except (ConnectionError, Timeout) as e:
            print('HtmlDownload ConnectionError or Timeout: ' + str(e))
            if retry_count > 0:
                self.down_html(url, retry_count - 1, headers, proxies, data)
            return None
        except Exception as e:
            print('HtmlDownload Exception: ' + str(e))