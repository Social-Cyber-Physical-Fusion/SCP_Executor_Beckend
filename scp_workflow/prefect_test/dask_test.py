# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/08 15:15:00
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   dask_test.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
from prefect import task, Flow
import datetime
import random
from time import sleep


@task
def inc(x):
    sleep(random.random() / 10)
    return x + 1


@task
def dec(x):
    sleep(random.random() / 10)
    return x - 1


@task
def add(x, y):
    sleep(random.random() / 10)
    return x + y


@task(name="sum")
def list_sum(arr):
    return sum(arr)


with Flow("dask-example") as flow:
    incs = inc.map(x=range(100))
    decs = dec.map(x=range(100))
    adds = add.map(x=incs, y=decs)
    total = list_sum(adds)

if __name__ == "__main__":
    flow.visualize()
    # flow.run()
    # from prefect.engine.executors import DaskExecutor

    # executor = DaskExecutor(address='tcp://10.222.161.158:8786')
    # flow.run(executor=executor)
