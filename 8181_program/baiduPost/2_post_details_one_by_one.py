import requests
import datetime
from pymysql import connect
from pymysql.cursors import DictCursor
from settings import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, \
                    MYSQL_DATABASE, HEADERS, TARGETS, MOST_POST_URLS
import time


class BaiduPost(object):
    def __init__(self):
        self.conn = connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset='utf8'
        )
        self.cursor = self.conn.cursor(DictCursor)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def return_fetchone(self, sql):
        self.cursor.execute(sql)
        flag = self.cursor.fetchone().get('count(*)')
        return flag

    def return_fetchall(self, sql):
        self.cursor.execute(sql)
        temps = self.cursor.fetchall()
        return temps

def post_url_to_baidu(id, baidu_url, url):
    now = datetime.datetime.now()
    try:
        # print("提交成功", ":",now.strftime('%Y-%m-%d %H:%M:%S'),":",url,"---id= ",id)
        res_newest = requests.post(url=baidu_url,headers=HEADERS,data=url)
        if res_newest.status_code == 200 :
            print("提交成功", ":",now.strftime('%Y-%m-%d %H:%M:%S'),":",url,"---id= ",id)
        else:
            print("提交失败", ":",now.strftime('%Y-%m-%d %H:%M:%S'),":",url,"---id= ",id)
            print(res_newest.text)
            time.sleep(24*60*60)
    except:
        print("提交错误", ":",now.strftime('%Y-%m-%d %H:%M:%S'),":",url,"---id= ",id)



def main():
    sql = "select count(*) from book_details"
    baidu = BaiduPost()
    flag = baidu.return_fetchone(sql)
    print(flag)
    for i in range(0, flag):
        sql = "select id, book_id,sort_id from book_details order by id desc limit {},{} ;".format(i,1)
        baidu = BaiduPost()
        temps = baidu.return_fetchall(sql)
        for temp in temps:
            for target in TARGETS:
                url = target.get('post_data')+str(temp.get('book_id'))+'/'+str(temp.get('sort_id'))
                post_url_to_baidu(str(temp.get('id')), target.get('post_url'), url)




if __name__ == '__main__':
    while True:
        main()
