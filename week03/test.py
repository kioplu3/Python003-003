#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Pool, Process, Lock, TimeoutError
import os
import time

def f(x):
    return x*x


def info(title):
    print(title)
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())

# process 类


def f(name):
    info('function f')
    print('hello', name)


def f_lock(l, i):
    l.acquire()
    try:
        print('hello world', i)
    # 注意这里的lock写法
    finally:
        l.release()


def f_pool(x):
    return x * x


if __name__ == '__main__':
    # with Pool(5) as p:
    #     print(p.map(f, [1, 2, 3]))
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

    with Pool(processes=4) as pool:
        print(pool.map(f_pool, range(10)))

        for i in pool.imap_unordered(f_pool,range(10)):
            print(i)

        res = pool.apply_async(f,(20,))
        print(res.get(timeout=1))

        multiple_results=[pool.apply_async(os.getpid, ()) for i in range(4)]

        print([res.get(timeout=1) for res in multiple_results])

        res = pool.apply_async(time.sleep, (10,))

        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("we laced patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    print("Now the pool is closed and no longer available")
