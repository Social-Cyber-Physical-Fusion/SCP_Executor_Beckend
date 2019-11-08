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
import json
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from utility.my_logger import MyLogger
from scp_model_def import ACTIONS_IN_SCP_META_MODEL
from scp_model_def import RESOURCES_IN_SCP_META_MODEL
from scp_modelparser.resource_instantiation import Resource_Instantiation

logger = MyLogger.get_logger()

class Model_Reader():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = ''
        self.model_desc = None
        self.model_json = ''
        self.actions = []
        self.resources = []

    def load_model_from_file(self, jsonfile_path):

        try:
            with open(jsonfile_path, 'rb') as f:
                self.model_json = f.read().decode()
            # print(type(self.model_json))
        except Exception as e:
            logger.error('error in {}, error : \n '.format(__file__, e))

        self.model_desc = json.loads(self.model_json)['childShapes']
        return self.model_desc

    def get_actions(self):
        for element in self.model_desc:
            if element['stencil'] in ACTIONS_IN_SCP_META_MODEL:
                self.acions.append(element)
        return self.actions

    def get_resources(self):
        for element in self.model_desc:
            if element['stencil'] in RESOURCES_IN_SCP_META_MODEL:
                self.resources.append(element)
        return self.resources


    def parser(self):
        
        logger.info(' Model {} Parsing. '.format(self.model_name))
        for action in self.actions:
            action_id = action['resourceId']
            name = action['name']

            # get related resources
            rel_resources = []

            Resource_Instantiation.get_instance_id_by_resource_id()
        



if __name__ == "__main__":
    mr = Model_Reader()
    mr.load_model_from_file('./5016.json')
    print(mr.model)
    # print(json.loads(test))
