# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/08 18:25:29
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   test4.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
from prefect import task, Flow
from datetime import timedelta
from prefect.schedules import IntervalSchedule

@task
def say_hello():
    print('Hello, world!')

schedule = IntervalSchedule(interval=timedelta(minutes=1))

with Flow('Hello', schedule) as flow:
    say_hello()

flow.run()