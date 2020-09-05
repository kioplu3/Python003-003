#!/usr/bin/env python
# coding=utf-8
import threading

class MyThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
    
    def run(self):
        print("current task: ", self.n)


if __name__ == "__main__":
    t1 = MyThread("thread 1")
    t2 = MyThread("thread 2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()
