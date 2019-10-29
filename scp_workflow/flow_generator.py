# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/29 14:50:11
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   flow_generator.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
from string import Template

BASE_PACKAGE = '''from prefect import Task'''

BASE_TEMPLATE = '''

class scp_task_$task_id(Task):

    def __init__(self, default: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default

    def run(self, x: int, y: int=None) -> int:
        if y is None:
            y = self.default
        return x + y

flow = Flow('$flow_name')

flow.run()
'''

class Flow_Template():

    def __init__(self):
        pass

if __name__ == "__main__":
    template_string = 'scp_task_$task_id():'
    s = Template(template_string)
    d = {'task_id': '1'}
    print(s.substitute(d))

