import gevent
from gevent import monkey

monkey.patch_all()
from gevent.pool import Pool
from multiprocessing.dummy import Pool as Thread
from common.logger import Logger
import time
import json
import requests


pool = Pool(200)  # 使用协程池


class NewProcessIdea(Logger):
    @staticmethod
    def just_draw(uid):
        """抽奖函数"""
        data = {
            "url": "/v3/groupChat/grantAuth",
            "host": "https://oversea.kuaishebao.com",
            "params": json.dumps({
                "uid": uid,
                "toUids": "",
                "groupId":9658,
                "role":2
            })
        }

        r = requests.post(url="http://sptestapitest.wb-intra.com/api/test", data=data)
        print(r.json())


    def corroutine_draw(self, uid):
        """创建加入协程"""
        all_corou = []
        for c in range(1000):
            all_corou.append(pool.spawn(self.just_draw, uid))
            gevent.joinall(all_corou)

    def run(self, uid):
        start_time = time.time()  # 开始时间
        self.corroutine_draw(uid)
        end_time = time.time()
        take_time = end_time - start_time

        if take_time < 1:
            # 判断不足一秒,设置为一秒
            take_time = 1
            # 计算花费时间
            m, s = divmod(take_time, 60)
            h, m = divmod(m, 60)

            self.write_log("花费时间 %02d:%02d:%02d"% (h, m, s))


    def main(self):
        """使用多线程执行程序"""
        np = Thread(10)
        uid_list = ["904047861"] * 3
        result = []
        for uid in uid_list:
            res = np.apply_async(self.run, (uid,))
            result.append(res)

        np.close()
        np.join()


import urllib.request
import gevent
from gevent import monkey

monkey.path_all()






class NewProcessIdeaAlex(Logger):
    @staticmethod
    def just_draw(uid):
        """抽奖函数"""
        print("UID:{}>>>>>>>>>>>>>开始时间：{}".format(uid, time.time()))
        data = {
            "url": "/v3/groupChat/grantAuth",
            "host": "https://oversea.kuaishebao.com",
            "params": json.dumps({
                "uid": uid,
                "toUids": "",
                "groupId":9658,
                "role":2
            })
        }

        r = requests.post(url="http://sptestapitest.wb-intra.com/api/test", data=data)
        print(r.json())
        print("UID:{}<<<<<<<<<<<<<结束时间：{}".format(uid, time.time()))


    def worker_genvent(self):
        """创建加入协程"""
        # all_corou = []
        # for c in range(1000):
        #     all_corou.append(pool.spawn(self.just_draw, uid))
        #     gevent.joinall(all_corou)
        # img_urls = []  # 在这里填写你要下载的图片地址
        gevent.joinall([gevent.spawn(self.just_draw, i) for i in range(1000)])

    def run(self):
        np = Thread(10)
        uid_list = ["904047861"] * 3
        result = []
        for uid in uid_list:
            res = np.apply_async(self.worker_genvent, (uid,))
            result.append(res)

        np.close()
        np.join()





from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))
    # random.random() 随机生成0～1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop-t_start))


po = Pool(3)  # 定义一个进程池，最大进程数3
for i in range(0, 10):
    # Pool().apply_async(要调用的目标， (传递给目标的参数元组,))
    # 每次循环将会用空闲出来的子进程去调用目标
    po.apply_async(worker, (i,))


print("--------start--------")
po.close()  # 关闭进程池，关闭后po不再接收新的请求
po.join()  # 等待po中的所有子进程执行完成，必须放在close()语句之后
print("---------end----------")





def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    img_urls = []  # 在这里填写你要下载的图片地址
    gevent.joinall([gevent.spawn(downloader, i+".jpg", i) for i in img_urls])


if __name__ == '__main__':
    main()
