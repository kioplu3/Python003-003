#!/usr/bin/env python
# coding=utf-8

import threading
import time


fork_lock = [threading.Lock() for i in range(5)]


class Philosopher(threading.Thread):

    def __init__(self, site_num):
        threading.Thread.__init__(self)
        self.site_num = site_num
        self.fork1 = site_num
        self.fork2 = (site_num - 1) if (site_num - 1) >= 0 else 4

    def eat(self):
        # 获取锁
        # 获取服务员的统一
        max_fork = max(self.fork1, self.fork2)
        min_fork = min(self.fork1, self.fork2)
        if fork_lock[max_fork].acquire(1) and fork_lock[min_fork].acquire(1):
            print("Philosopher {} is eating".format(self.site_num))
            fork_lock[min_fork].release()
            fork_lock[max_fork].release()

    def thinking(self):
        print("Philosopher {} is thinking".format(self.site_num))
        time.sleep(1)
        pass

    def run(self):
        while 1:
            self.eat()
            self.thinking()

    def __repr__(self):
        return 'p {} use {} {} forks'.format(self.site_num, self.fork1,
                                             self.fork2)


# test = [Philosopher(i) for i in range(1, 6)]

if __name__ == '__main__':
    philos = [Philosopher(i) for i in range(5)]
    print(philos)
    for i in range(0, 5):
        philos[i].start()
