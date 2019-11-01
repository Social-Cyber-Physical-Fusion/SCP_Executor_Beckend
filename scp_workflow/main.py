# -*-coding:utf8-*-
import json
import pymongo
from bson.json_util import loads,dumps
from flask import Flask, request
from flask_cors import CORS
from scp_workflow.service.app_service import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
myclient = pymongo.MongoClient("mongodb://129.211.10.118:27017/")
# dblist = myclient.list_database_names()
db_hcp = myclient["db_hcp"]
t_app_class = db_hcp["t_app_class"]
t_app_instance = db_hcp["t_app_instance"]


# 保存app_class
@app.route('/save_app_class', methods={'POST', 'GET'})
def save_app_class():
    app_class = json.loads(request.data)
    app_class_id = insert_app_class(t_app_class, app_class)
    return app_class_id


# 读取所有app_class的id name time
@app.route('/get_all_app_class_introduction', methods={'POST', 'GET'})
def get_all_app_class_introduction():
    app_classes_introduction = find_all_app_class_introduction(t_app_class)
    data = dumps(app_classes_introduction)
    response = make_response(data, 200)
    # app = json.loads(data)
    return response


# 读取所有app_class
@app.route('/get_all_app_class', methods={'POST', 'GET'})
def get_all_app_class():
    app_classes = find_all_app_class(t_app_class)
    response = make_response(str(app_classes), 200)
    return response


# 保存app_instance
@app.route('/save_app_instance', methods={'POST', 'GET'})
def save_app_instance():
    app_instance = json.loads(request.data)
    app_instance_id = insert_app_instance(t_app_instance, app_instance)
    return app_instance_id

# 删除app_instance
# 修改app_instance
# 查询app_instance


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
