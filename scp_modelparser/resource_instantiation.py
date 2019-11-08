# -*- coding: utf-8 -*-
'''
@Time    :   2019/10/30 01:39:14
@Author  :   Tianyi Wu 
@Contact :   wutianyi@hotmail.com
@File    :   resource_instantiation.py
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
import py2neo

neo4j_config = {'user': '', 'password': ''}


class Resource_Instantiation():
    def __init__(self):
        self.model = None

    def set_model(self, model):
        self.model = model

    def resource_instantiate(self):
        pass

    def query_knowledge_graph(self):
        pass

    def get_instance_id_by_resource_id(self, resource_id=None):
        return 'resource id'

    def get_resourece_info_by_instance_id(self, instance_id=None):
        resource_info = {}
        return resource_info