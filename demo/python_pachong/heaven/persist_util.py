import dbm
import pickle
import os

'''
数据持久化工具类
'''


class PersistUtil(object):
    def save_data(self, name='No Name', urls=None):
        if urls is None or len(urls) <= 0:
            return
        try:
            history_db = dbm.open('downloader_history', 'c')
            history_db[name] = str(urls)
        finally:
            history_db.close()

    def get_data(self):
        history_links = set()
        try:
            history_db = dbm.open('downloader_history', 'r')
            for key in history_db.keys():
                history_links.add(str(history_db[key], 'gbk'))
        except Exception as e:
            print('遍历dbm数据失败: ' + str(e))
        return history_links

    # 使用pickle保存历史下载记录
    def save_history_links(self, urls):
        if urls is None or len(urls) <= 0:
            return
        with open('DownloaderHistory', 'wb') as pickle_file:
            pickle.dump(urls, pickle_file)

    # 获取保存在pickle中的历史下载记录
    def load_history_links(self):
        if os.path.exists('DownloaderHistory'):
            with open('DownloaderHistory', 'rb') as pickle_file:
                return pickle.load(pickle_file)
        else:
            return None