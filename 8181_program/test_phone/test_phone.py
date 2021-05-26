from settings import TEST_URL_ALI, WRONG_PROVINCES, WRONG_CATNAMES
from requests import request
import demjson


class TestPhone(object):
    """docstring for TestPhone"""
    def __init__(self, filename_url):
        """
        初始化整个类：
        """
        self.test_url = TEST_URL_ALI
        self.wrong_provinces = WRONG_PROVINCES
        self.wrong_catnames = WRONG_CATNAMES
        self.filename_url = filename_url
        self.headers = {
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
        }
        self.total_phone = 0
        self.right_phone = 0
        self.wrong_phone = 0

    def empty_files(self):
        """
        清空所有需要用到的文件
        """
        with open('right_phone.txt', "r+") as f:
            read_data = f.read()
            f.seek(0)
            f.truncate()   #清空文件

        with open('wrong_phone.txt', "r+") as f:
            read_data = f.read()
            f.seek(0)
            f.truncate()   #清空文件

    def right_phone(self, phoneNum):
        """
        正确电话号码处理方法
        """
        pass

    def wrong_phone(self, phoneNum):
        """
        错误电话号码处理方法
        """
        pass

    def is_valid_phone(self, phoneNum):
        """
        是否是有效的电话号码
        True： 有效
        Flase： 无效
        """
        get_url = self.test_url + phoneNum
        # print("get_url = ", get_url)
        rep = request("get", get_url, headers=self.headers)
        str1 = rep.text
        # print("str1 = ", str1)
        str2 = str1[str1.find("{"):str1.find("}")+1]
        # print("str2 = ", str2)
        json3 = demjson.decode(str2)
        # print("json3 = ", json3)
        # print("type(json3) = ", type(json3))
        print("这个号码的所属运营商 : ", json3.get("catName"))
        if json3.get("catName") in WRONG_CATNAMES:
            self.wrong_phone(json3.get("telString"))
            return False
        print("这个号码所属的省份 : ", json3.get("province"))
        if json3.get("province") in WRONG_PROVINCES:
            self.wrong_phone(json3.get("telString"))
            return False
        self.right_phone(json3.get("telString"))
        return True

    def run(self):
        print("清空所有文件")
        # 清空所有文件
        self.empty_files()
        # 按行读取数据
        with open(self.filename_url) as file:
            for line in file:
                self.total_phone += 1
                print("line = ", line)
                if self.is_valid_phone(line):
                    # 返回True：是可以用的号码
                    self.right_phone += 1
                else:
                    # 返回False：是不可以用的号码
                    self.wrong_phone += 1

        print("一共有{ ",self.total_phone," }个号码，能用的有{ ",self.right_phone," }个号码，不能用的有{ ",self.wrong_phone," }个号码")





# with open('filename') as file:
#     for line in file:
#         do_things(line)


# with open('right_phone.txt', "r+") as f:
#     read_data = f.read()
#     f.truncate()   #清空文件


def main():
    print("进入main")
    tp = TestPhone("test.txt")
    tp.run()

if __name__ == '__main__':
    print("开始执行!")
    main()
    print("结束执行!")
