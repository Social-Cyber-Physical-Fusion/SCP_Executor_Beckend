# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/30 17:03:50
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   app_in_docker.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
from prefect import Flow
from prefect.tasks.docker import (
    CreateContainer,
    StartContainer,
    GetContainerLogs,
    WaitOnContainer,
)
from prefect.triggers import always_run

flow_code = ''

container = CreateContainer(
    image_name='prefecthq/prefect',
    command='''python -c "from prefect import task, Flow
from datetime import timedelta
from prefect.schedules import IntervalSchedule

@task
def say_hello():
    print('Hello, world!')

schedule = IntervalSchedule(interval=timedelta(minutes=1))

with Flow('Hello', schedule) as flow:
    say_hello()

flow.run()"''',
)

start = StartContainer()
logs = GetContainerLogs(trigger=always_run)
status_code = WaitOnContainer()

flow = Flow('Run in Docker')

## set individual task dependencies using imperative API
start.set_upstream(container, flow=flow, key='container_id')
logs.set_upstream(container, flow=flow, key='container_id')
status_code.set_upstream(container, flow=flow, key='container_id')

status_code.set_upstream(start, flow=flow)
logs.set_upstream(status_code, flow=flow)

## run flow and print logs
flow_state = flow.run()

print('=' * 30)
print('Container Logs')
print('=' * 30)
print(flow_state.result[logs].result)