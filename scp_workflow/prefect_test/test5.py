# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/08 23:24:43
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   test5.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
import random
from prefect import Flow, task


@task
def a_number():
    temp = random.randint(0, 100)
    print(temp)
    return temp


@task
def get_sum(x):
    temp = sum(x)
    print(temp)
    return temp


with Flow('Using Collections') as flow:
    a = a_number()
    b = a_number()
    s = get_sum([a, b])


if __name__ == "__main__":
    flow.run()
    print(a)
    print(b)
    print(s)
