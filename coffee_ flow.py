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

class Scp_Task(Task):
    def __init__(self, name=None, **input=None):
        super().__init__(name=name)
        self.action_desc = ''
        self.related_resoureces = []
        self.type = ''

    def run(self, **input):
        if self.type == 'CloudApp':
            url = input['url']
            r = requests.post(self.url, json=input)
            output = r.json()
            return output



flow = Flow("Run a Prefect Flow in Docker")

input_1 = {
    'url': '',
    'coffee order id': '',
}

scp_task_1 = Scp_Task('点咖啡')



scp_task_2 = Scp_Task('做咖啡')
scp_task_3 = Scp_Task('咖啡完成')
scp_task_4 = Scp_Task('取杯子')
scp_task_5 = Scp_Task('取咖啡')
scp_task_6 = Scp_Task('送咖啡')
