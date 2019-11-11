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
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

from utility.my_logger import MyLogger
from string import Template

logger = MyLogger.get_logger()

FLOW_ADD_TASK = '''flow.add($task_identifier)'''
FLOW_CONFIG = '''flow = Flow('$flow_name')'''
FLOW_START = '''flow.run()'''

class Flow_Template():
    def __init__(self):
        pass


if __name__ == "__main__":
    template_string = 'scp_task_$task_id():'
    s = Template(template_string)
    d = {'task_id': '1'}
    print(s.substitute(d))

    # logger = MyLogger.get_logger()
    logger.info(s.substitute(d))
