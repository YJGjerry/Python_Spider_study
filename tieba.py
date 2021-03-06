#第一次尝试理解“面向对象”的编程方法 构造class，使用编程逻辑，爬取贴吧
import requests

class tiebaspyder:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name #非必须
        self.url_temp = "https://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}

    def get_url_list(self):#构造url列表
        # url_list = []
        # for i in range(1000):
        #     url_list.append(self.url_temp.format(i*50))
        # return url_list
        return [self.url_temp.format(i*50) for i in range(1000)]  #‘编程式’ 以后应用更大 代码不臃肿，建议使用

    def parse_url(self,url):#历遍，发送请求，获取相应
        response = requests.get(url,headers = self.headers)
        return response.content.decode()

    def save_html(self,html_str,page_num):#3 保存
        file_path = "{}-第{}页.html".format(self.tieba_name,page_num)
        with open(file_path,"w",encoding="utf-8") as f: #格式化"'漫威'-第1页.html" encoding=utf-8 重点
            f.write(html_str)

    def run(self):#实现主要逻辑,即主要思路步骤
        #1 构造url_list
        url_list = self.get_url_list()
        #2 历遍，发送请求，获取相应
        for url in url_list:
            html_str = self.parse_url(url)
            #3 保存
            page_num = url_list.index(url)+1   #页码数
            self.save_html(html_str,page_num)

if __name__ == '__main__':
    tiebaspyder =tiebaspyder('漫威')
    tiebaspyder.run()
