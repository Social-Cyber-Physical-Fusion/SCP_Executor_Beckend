# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/25 14:32:30
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   scp_task.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
from prefect import Task


class SCPTask(Task):
    def __init__(self, **kwargs):
        super.__init__(**kwargs)

        self.task_id = ''
        self.resource_ids = []

    def run(self):
        return requests.get(url, auth=(self.username, self.password))

    def get_task_resources(self, task_id):
        return self.resource_ids


flow.add(task)