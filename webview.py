import requests
import time
import os
import re
import filecmp

class Webview:
    def __init__(self, url, oripage, request=None, file_dir=None, headers=None):
        self.url = url 
        self.oripage_path = oripage
        
        if not request:
            self.requests = requests.session()
        else:
            self.requests = request
            
        if not file_dir: 
            self.dir = './image/'
        else:
            self.dir = file_dir
            
        if not headers: 
            self.headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip,deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
            }
        else:
            self.headers = headers

    def save_file0(self, url=None):
        if url is not None:
            self.url = url
        if not self.url:
            return False
        size = 0
        
        while size == 0:
            web_file = self.requests.get(url=self.url, headers=self.headers)

            web_path = self.dir + 'oripage'

            with open(web_path, 'wb') as f:
                f.write(web_file.content)

            size = os.path.getsize(web_path)
            if size == 0:
                os.remove(web_path)

        return web_path if (size > 0) else False

    def save_file(self, url=None):
        if url is not None:
            self.url = url
        if not self.url:
            return False
        size = 0
        
        while size == 0:
            web_file = self.requests.get(url=self.url, headers=self.headers)

            web_path = self.web_path(web_file.headers)

            with open(web_path, 'wb') as f:
                f.write(web_file.content)

            size = os.path.getsize(web_path)
            if size == 0:
                os.remove(web_path)

        return web_path if (size > 0) else False

    def web_path(self, header):
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        file_name = 'newpage'

        return self.dir + file_name

    def web_diff(self):
        return filecmp.cmp(self.oripage_path, str(self.save_file()))


if __name__ == '__main__':
    page = Webview(url = 'http://www.suda.edu.cn', oripage = "C:/Users/庄依林/OneDrive/桌面/Code/class/webview/oriweb", file_dir = 'C:/Users/庄依林/OneDrive/桌面/Code/class/webview/')
    print(page.web_diff())