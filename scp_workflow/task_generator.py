# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/31 08:39:51
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   task_generator.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

from utility.my_logger import MyLogger
from string import Template
from prefect import Task

logger = MyLogger.get_logger()

PACKAGE_TEMPLATE = '''from prefect import Task'''

TASK_TEMPLATE = '''
class scp_task_$task_id(Task):

    def __init__(self, default: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default

    def run(self, $input, $output):
        return $output

    @classmethod
    def get_resource_id(self):
        return current_resource_id()
'''

class TaskTemplate():
    def __init__(self):
        self.resource_id = None

    def get_task():
        pass



