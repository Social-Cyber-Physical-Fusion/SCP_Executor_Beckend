# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/21 00:58:32
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   model_reader.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
import pymongo
from bson.objectid import ObjectId

import json
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from utility.my_logger import MyLogger
from scp_model_def import ACTIONS_IN_SCP_META_MODEL
from scp_model_def import RESOURCES_IN_SCP_META_MODEL



logger = MyLogger.get_logger()

class Model_Reader():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = ''

        self.actions = []
        self.resources = []
        self.app_class = None
        self.app_class_instance = None
        

    def load_model_from_file(self, jsonfile_path):

        try:
            with open(jsonfile_path, 'rb') as f:
                model_json = f.read().decode()
            # print(type(self.model_json))
        except Exception as e:
            logger.error('error in {}, error : \n '.format(__file__, e))

        self.app_class = json.loads(model_json)
        return self.app_class

    def load_app_from_mongodb(self, object_id=None):

        # 初始化Mongo
        myclient = pymongo.MongoClient("mongodb://129.211.10.118:27017/")
        db_hcp = myclient.db_hcp

        app_class_table = db_hcp['t_app_class']
        app_class_instance_table = db_hcp['t_app_instance']
        self.app_class = app_class_table.find_one({'_id':ObjectId(object_id)})
        self.app_class_instance = app_class_instance_table.find_one({'app_class_id':ObjectId(object_id)})
        return self.app_class, self.app_class_instance

    def get_actions(self):
        for element in self.app_class['childShapes']:
            if element['stencil'] in ACTIONS_IN_SCP_META_MODEL:
                self.acions.append(element)
        return self.actions

    def get_resources(self):
        for element in self.app_class['childShapes']:
            if element['stencil'] in RESOURCES_IN_SCP_META_MODEL:
                self.resources.append(element)
        return self.resources


    def parser(self):
        
        logger.info(' Model {} Parsing. '.format(self.model_name))
        for action in self.actions:
            action_id = action['resourceId']
            name = action['name']

            # get related resources in current action
            rel_resources = []

            # get instantiation

            
            # generate task


            # 


        # generate flow

    

    def get_resource_instance_id(self):
        pass        



if __name__ == "__main__":
    mr = Model_Reader()
    mr.load_app_from_mongodb('5dc676d0cf8281e61ea98e76')

    # print(mr.app_class)
    # print('=' * 20)
    # print(mr.app_class_instance)

    