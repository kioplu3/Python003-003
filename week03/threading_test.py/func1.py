#!/usr/bin/env python
# coding=utf-8

import threading


def run(n):
    print("cunrrent task: ", n)


if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=("thread 1",))
    t2 = threading.Thread(target=run, args=("thread 2",))
    t1.start()
    t2.start()

 
