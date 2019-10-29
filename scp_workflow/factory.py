# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/25 12:46:07
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   factory.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

from prefect import task, Flow


class Factory():
    def __init__():
        pass

    factory = {
        'flow_factory': FlowFactory,
        'task_factory': TaskFactory,
    }

    @classmethod
    def get(cls, factory_name):
        factory = cls.factory.get(factory_name)
        return factory


class FlowFactory():
    '''
    Flowfactory    
    '''

    def __str__(self):
    return 'flow factory'

    def create_flow(self, **flow_name=None):
        return Flow(flow_name)

    

class TaskFactory():
    '''
    TaskFactory
    '''

    def __str__(self):
        return 'task factory'

    def create_task(self, **task_info=None):
        return task
