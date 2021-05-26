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


NewProcessIdea().main()
