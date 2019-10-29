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


class model_reader():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = None
        self.model_json = ''
        self.actions = None

    def load_model_from_file(self, jsonfile_path):
        with open(jsonfile_path, 'rb') as f:
            self.model_json = f.read().decode()
            # print(type(self.model_json))

        self.model = json.loads(self.model_json)
        return self.model

    def get_child_shapes(self):
        return self.model['childShapes']


if __name__ == "__main__":
    mr = model_reader()
    mr.load_model_from_file('./model.json')

    print(type(mr.model))
    print(mr.model)
    # print(json.loads(test))
