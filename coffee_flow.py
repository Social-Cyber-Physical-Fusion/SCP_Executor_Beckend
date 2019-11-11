# -*- coding: utf-8 -*-
'''
@Time    :   2019/11/01 20:47:50
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   coffee_ flow.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
from prefect import Task, Flow
import requests
import time


class Scp_StartEvent_Task(Task):
    def run(self):
        pub_to_MQ({'msg': 'flow start', 'flow id': ''})


class Scp_EndEvent_Task(Task):
    def run(self):
        pub_to_MQ({'msg': 'flow end', 'flow id': ''})


class Scp_Task(Task):
    def __init__(self, name: str, **config):
        super().__init__(name=name)
        self.action_desc = ''
        self.task_type = config.get('task_type')
        self.task_name = config.get('task_name')
        self.task_id = config.get('task_id')

    def run(self, **input):
        '''
        任务执行
        '''
        output = None
        # 推送任务开始消息到中间件
        pub_to_MQ({
            'msg': 'task start',
            'task step': self.task_name,
            'flow_id': self.task_id
        })

        url = input.get('url')
        if url:
            r = requests.post(self.url, json=input)
            output = r.json()

        # 推送任务结束消息到中间件
        pub_to_MQ({
            'msg': 'task end',
            'task step': self.task_name,
            'flow_id': self.task_id
        })
        return output


# task = Scp_Task(name = 'default task')


class Scp_Event_Task(Task):
    def __init__(self, name, **config):
        super().__init__(name=name)
        self.action_desc = ''
        self.task_type = config.get('task_type')
        self.task_name = config.get('task_name')
        self.task_id = config.get('task_id')

    def run(self, **input):
        '''
        任务执行
        '''
        output = None
        # 推送任务开始消息到中间件
        pub_to_MQ({
            'msg': 'task start',
            'task step': self.task_name,
            'flow_id': self.task_id
        })

        # 等待MQ消息
        while True:
            print(5, 's')
            time.sleep(5)
            print(10, 's')
            time.sleep(5)
            break

        # 推送任务结束消息到中间件
        pub_to_MQ({
            'msg': 'task end',
            'task step': self.task_name,
            'flow_id': self.task_id
        })

        return output


# event = Scp_Event_Task(name = 'default event')


def pub_to_MQ(self, **msg):
    '''
    向MQ推送消息
    '''
    print(msg.get('msg'))


def exception_handler(state, cur_task):
    '''
    流程的异常处理
    '''
    task_state = state.result[cur_task]
    assert task_state.is_successful()


if __name__ == "__main__":

    flow = Flow("Run a Prefect Flow in Docker")

    # 点咖啡 task
    # task_config_1 = {
    #     'task_type':'action',
    #     'task_name':'',
    #     'task_id':'',
    #     'coffee order id': '',
    # }
    # task_1 = Scp_Task('点咖啡', task_config_1)

    task_config_1 = {
        'task_type': 'action',
        'task_name': 'make coffee',
        'task_id': '',
    }
    task_1 = Scp_Task(name='make coffee', **task_config_1)

    task_config_2 = {
        'task_type': 'event',
        'task_name': 'coffee finished',
        'task_id': '',
    }
    # task_2 = Scp_Task.copy()
    task_2 = Scp_Event_Task(name='coffee finished', **task_config_2)

    task_config_3 = {
        'task_type': 'action',
        'task_name': 'send coffee',
        'task_id': '',
    }
    task_3 = Scp_Task(name='send coffee', **task_config_3)

    # add tasks to the flow
    flow.add_task(Scp_StartEvent_Task())
    flow.add_task(task_1)
    flow.add_task(task_2)
    flow.add_task(task_3)
    flow.add_task(Scp_EndEvent_Task())

    # create non-data dependencies
    # task_2.set_upstream(task_1, flow=flow)
    task_3.set_upstream(task_2, flow=flow)
    # task_4.set_upstream(task_3, flow=flow)

    # create data bindings
    task_input_1 = {
        'msg': 'test_task_1',
        'url': '',
    }
    task_input_3 = {
        'msg': 'test_task_2',
        'url': '',
    }
    task_1.bind(**task_input_1, flow=flow)
    task_3.bind(**task_input_3, flow=flow)

    # start flow
    state = flow.run()
