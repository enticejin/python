from demo.python_pachong.heaven import url_manager, html_parser, html_download, persist_util
from tkinter import *
from threading import Thread
import os
# https://www.dytt8.net/html/gndy/dyzz/index.html 下载地址

class SpiderMain(object):
    def __init__(self):
        self.mUrlManager = url_manager.UrlManager()
        self.mHtmlParser = html_parser.HtmlParser()
        self.mHtmlDownload = html_download.HtmlDownload()
        self.mPersist = persist_util.PersistUtil()

    # 加载历史下载链接
    def load_history(self):
        history_download_links = self.mPersist.load_history_links()
        if history_download_links is not None and len(history_download_links) > 0:
            for download_link in history_download_links:
                self.mUrlManager.add_download_url(download_link)
                d_log("加载历史下载链接: " + download_link)

    # 保存历史下载链接
    def save_history(self):
        history_download_links = self.mUrlManager.get_download_url()
        if history_download_links is not None and len(history_download_links) > 0:
            self.mPersist.save_history_links(history_download_links)

    def craw_movie_links(self, root_url, score=8):
        count = 0;
        self.mUrlManager.add_url(root_url)
        while self.mUrlManager.has_continue():
            try:
                count = count + 1
                url = self.mUrlManager.get_url()
                d_log("craw %d : %s" % (count, url))
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
                    'Referer': url
                }
                content = self.mHtmlDownload.down_html(url, retry_count=3, headers=headers)
                if content is not None:
                    doc = content.decode('gb2312', 'ignore')
                    movie_urls, next_link = self.mHtmlParser.parser_movie_link(doc)
                    if movie_urls is not None and len(movie_urls) > 0:
                        for movie_url in movie_urls:
                            d_log('movie info url: ' + movie_url)
                            content = self.mHtmlDownload.down_html(movie_url, retry_count=3, headers=headers)
                            if content is not None:
                                doc = content.decode('gb2312', 'ignore')
                                movie_name, movie_score, movie_xunlei_links = self.mHtmlParser.parser_movie_info(doc,
                                                                                                                 score=score)
                                if movie_xunlei_links is not None and len(movie_xunlei_links) > 0:
                                    for xunlei_link in movie_xunlei_links:
                                        # 判断该电影是否已经下载过了
                                        is_download = self.mUrlManager.has_download(xunlei_link)
                                        if is_download == False:
                                            # 没下载过的电影添加到迅雷下载列表
                                            d_log('开始下载 ' + movie_name + ', 链接地址: ' + xunlei_link)
                                            self.mUrlManager.add_download_url(xunlei_link)
                                            os.system(
                                                r'"D:/Program Files (x86)/Thunder Network/Thunder/Program/Thunder.exe" {url}'.format(url=xunlei_link))
                                            # 每下载一部电影都实时更新数据库，这样可以保证即使程序异常退出也不会重复下载该电影
                                            self.save_history()
                    if next_link is not None:
                        d_log('next link: ' + next_link)
                        self.mUrlManager.add_url(next_link)
            except Exception as e:
                d_log('错误信息: ' + str(e))


def runner(rootLink=None, scoreLimit=None):
    if rootLink is None:
        return
    spider = SpiderMain()
    spider.load_history()
    if scoreLimit is None:
        spider.craw_movie_links(rootLink)
    else:
        spider.craw_movie_links(rootLink, score=float(scoreLimit))
    spider.save_history()


# rootLink = 'https://www.dytt8.net/html/gndy/dyzz/index.html'
# rootLink = 'https://www.dytt8.net/html/gndy/dyzz/list_23_207.html'
def start(rootLink, scoreLimit):
    loop_thread = Thread(target=runner, args=(rootLink, scoreLimit,), name='LOOP THREAD')
    # loop_thread.setDaemon(True)
    loop_thread.start()
    # loop_thread.join() # 不能让主线程等待，否则GUI界面将卡死
    btn_start.configure(state='disable')


# 刷新GUI界面，文字滚动效果
def d_log(log):
    s = log + '\n'
    txt.insert(END, s)
    txt.see(END)


if __name__ == "__main__":
    rootGUI = Tk()
    rootGUI.title('XX电影自动下载工具')
    # 设置窗体背景颜色
    black_background = '#000000'
    rootGUI.configure(background=black_background)
    # 获取屏幕宽度和高度
    screen_w, screen_h = rootGUI.maxsize()
    # 居中显示窗体
    window_x = (screen_w - 640) / 2
    window_y = (screen_h - 480) / 2
    window_xy = '640x480+%d+%d' % (window_x, window_y)
    rootGUI.geometry(window_xy)

    lable_link = Label(rootGUI, text='解析根地址: ', \
                       bg='black', \
                       fg='red', \
                       font=('宋体', 12), \
                       relief=FLAT)
    lable_link.place(x=20, y=20)

    lable_link_width = lable_link.winfo_reqwidth()
    lable_link_height = lable_link.winfo_reqheight()

    input_link = Entry(rootGUI)
    input_link.place(x=20 + lable_link_width, y=20, relwidth=0.5)

    lable_score = Label(rootGUI, text='电影评分限制: ', \
                        bg='black', \
                        fg='red', \
                        font=('宋体', 12), \
                        relief=FLAT)
    lable_score.place(x=20, y=20 + lable_link_height + 10)

    input_score = Entry(rootGUI)
    input_score.place(x=20 + lable_link_width, y=20 + lable_link_height + 10, relwidth=0.3)

    btn_start = Button(rootGUI, text='开始下载', command=lambda: start(input_link.get(), input_score.get()))
    btn_start.place(relx=0.4, rely=0.2, relwidth=0.1, relheight=0.1)

    txt = Text(rootGUI)
    txt.place(rely=0.4, relwidth=1, relheight=0.5)

    rootGUI.mainloop()