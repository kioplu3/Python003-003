#!/usr/bin/env python
# coding=utf-8

import threading
import time

mutex_arbitrator = threading.Lock()

fork_states = [0] * 5

fork_lock = [threading.Lock() for i in range(5)]


def ask_fork(fork1, fork2):
    result = False
    if mutex_arbitrator.acquire(1):
        if fork_states[fork1] == 0 and fork_states[fork2] == 0:
            fork_states[fork1] = 1
            fork_states[fork2] = 1
            result = True
        mutex_arbitrator.release()
    return result


def release_fork(fork1, fork2):
    if mutex_arbitrator.acquire(1):
        fork_states[fork1] = 0
        fork_states[fork2] = 0
    mutex_arbitrator.release()


class Philosopher(threading.Thread):

    def __init__(self, site_num):
        threading.Thread.__init__(self)
        self.site_num = site_num
        self.fork1 = site_num
        self.fork2 = (site_num - 1) if (site_num - 1) >= 0 else 4

    def eat(self):
        # 获取锁
        # 获取服务员的统一
        ask = ask_fork(self.fork1, self.fork2)
        if ask:
            if fork_lock[self.fork1].acquire(1) and fork_lock[self.fork2].acquire(1):
                print("Philosopher {} is eating".format(self.site_num))
                fork_lock[self.fork1].release()
                fork_lock[self.fork2].release()
                release_fork(self.fork1, self.fork2)
        pass

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
