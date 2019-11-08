# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/25 10:59:09
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   logger.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
import logging

# logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    filemode='w',
                    filename='log.log',
                    level=logging.INFO)


class MyLogger():

    @classmethod
    def get_logger(self):
        return logging.getLogger()
