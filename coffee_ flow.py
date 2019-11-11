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

class Scp_Task(Task):
    def __init__(self, name=None, **config=None):
        super().__init__(name=name)
        self.action_desc = ''
        self.task_type = config['task_type']
        self.task_name = config['task_name']
        self.task_id = config['task_id']

    def run(self, **input):
        '''
        任务执行
        '''

        # 推送任务开始消息到中间件
        pub_to_MQ({'msg':'task start', 'task step':self.task_name, 'flow_id': self.task_id})

        url = input['url']
        r = requests.post(self.url, json=input)
        output = r.json()

        # 推送任务结束消息到中间件
        pub_to_MQ({'msg':'task end', 'task step':self.task_name ,'flow_id': self.task_id})
        return output

    def pub_to_MQ(self, msg):
        '''
        向MQ推送消息
        '''
class Scp_EventTask(Task):
    def __init__(self, name=None, **config=None):
        super().__init__(name=name)
        self.action_desc = ''
        self.task_type = config['task_type']
        self.task_name = config['task_name']
        self.task_id = config['task_id']

    def run(self, **input):
        '''
        任务执行
        '''

        # 推送任务开始消息到中间件
        pub_to_MQ({'msg':'task start', 'task step':self.task_name, 'flow_id': self.task_id})

        # 等待MQ消息
        while True:
            time.sleep(5)

        # 推送任务结束消息到中间件
        pub_to_MQ({'msg':'task end', 'task step':self.task_name ,'flow_id': self.task_id})
        return output

    def pub_to_MQ(self, msg):
        '''
        向MQ推送消息
        '''

def exception_handler(state, cur_task):
    '''
    流程的异常处理
    '''
    task_state = state.result[cur_task]
    assert task_state.is_successful()


if __name__ == "__main__": 

    flow = Flow("Run a Prefect Flow in Docker")

    # 点咖啡 task
    task_config_1 = {
        'task_type':'action',
        'task_name':'',
        'task_id':'',
        'url': '',
        'coffee order id': '',
    }
    task_1 = Scp_Task('点咖啡', task_config_1)

    task_config_2 = {
        'task_type':'action',
        'task_name':'',
        'task_id':'',
        'url': '',
        'coffee order id': '',
    }
    task_2 = Scp_EventTask('做咖啡', task_config_2)

    task_config_3 = {
        'task_type':'event',
        'task_name':'',
        'task_id':'',
        'url': '',
        'coffee order id': '',
    }
    task_3 = Scp_Task('咖啡完成', task_config_3)

    task_config_4 = {
        'task_name':'action',
        'task_id':'',
        'url': '',
        'coffee order id': '',
    }
    task_4 = Scp_Task('送咖啡', task_config_4)
    
    # add tasks to the flow
    flow.add_task(task_1)
    flow.add_task(task_2)    
    flow.add_task(task_3)    
    flow.add_task(task_4)    

    # create non-data dependencies
    task_2.set_upstream(task_1, flow=flow)
    task_3.set_upstream(task_2, flow=flow)
    task_4.set_upstream(task_3, flow=flow)

    # create data bindings
    task_input_1 = {
        'url': '',
    }

    task_input_2 = {
        'url': '',
    }
    task_input_4 = {
        'url': '',
    }
    task_1.bind(task_input_1, flow=flow)
    task_2.bind(task_input_2, flow=flow)
    task_4.bind(task_input_4, flow=flow)
    
    # start flow 
    state = flow.run()
