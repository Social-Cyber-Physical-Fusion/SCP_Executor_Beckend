# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/09 16:45:34
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   agent.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
from prefect.agent import LocalAgent

LocalAgent().start()