import time
import gevent
from gevent import monkey
from multiprocessing import Pool
import random


class NewProcessIdeaAlex(object):
    @staticmethod
    def just_draw(uid, pool_id):
        """抽奖函数"""
        for i in range(30):
            print("UID:{}   pool_id:{}   gevent_id:{}".format(uid, pool_id, i))
            time.sleep(random.randint(0,100)/100)


    def worker_genvent(self, uid):
        """创建加入协程"""
        gevent.joinall([gevent.spawn(self.just_draw, uid, i) for i in range(1000)])


    def run(self):
        np = Pool(100)
        # 下面这行你自己改
        uid_list = ["111111111","22222222", "333333333"]
        for uid in uid_list:
            res = np.apply_async(self.worker_genvent, (uid,))

        np.close()
        np.join()

if __name__ == '__main__':
    npia = NewProcessIdeaAlex()
    npia.run()
