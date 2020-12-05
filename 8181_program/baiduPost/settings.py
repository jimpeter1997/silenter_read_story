MYSQL_HOST = '222.186.173.204'
MYSQL_PORT = 3306
MYSQL_USER = 'alex1943'
MYSQL_PASSWORD = 'AlexHunter0451392aa##'
MYSQL_DATABASE = 'books'

# 一般这个HEADERS不用变，但是最好去百度站长后台确认一下
HEADERS = {
        'User-Agent': 'curl/7.12.1',
        'Host': 'data.zz.baidu.com',
        'Content-Type': 'text/plain',
        'Content-Length': '83'
}

"""
TARGETS是一个数组（为了方便以后多个网站提交内容）
    数组中的元素是字典：
        post_url是需要提交到的地址（必须去百度站长后台确认）
        post_data是你希望百度爬虫能来爬的链接（往往需要和数据库中的内容进行拼接）
        post_url和post_data，这两个键值不要变
"""
TARGETS = [
    {
        "post_url": "http://data.zz.baidu.com/urls?site=www.mingyueshuba.com&token=6qRDgyCXUvFYi4RY",
        "post_data": "https://www.mingyueshuba.com/book/"
    }
]

MOST_POST_URLS = 3000
