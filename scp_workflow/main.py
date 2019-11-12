# -*-coding:utf8-*-
import json
import time
import pymongo
from bson.json_util import loads, dumps
from flask import Flask, request, jsonify
from flask_cors import CORS
from scp_workflow.service.app_service import *
from scp_workflow.util.mongodb import *
from coffee_flow import Coffee_Flow

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
    data = request.data.replace(b"$$", b"")
    app_class = json.loads(data)
    app_class_id = insert_app_class(t_app_class, app_class)
    data = {'app_class_id': str(app_class_id)}
    return jsonify(data)


# 读取所有app_class的简单介绍
@app.route('/get_all_app_class_introduction', methods={'POST', 'GET'})
def get_all_app_class_introduction():
    app_classes_introduction = find_all_app_class_introduction(t_app_class)
    app_classes_introduction = get_id_str(app_classes_introduction)
    data = {'app_classes_introduction': app_classes_introduction}
    return jsonify(data)


# 获取一个app_class的详细流程
@app.route('/get_app_class_by_id', methods={'POST', 'GET'})
def get_app_class_by_id():
    app_class_id = request.values.get("app_class_id")
    app_class = find_app_class_by_id(t_app_class, app_class_id)
    app_class = get_id_str(app_class)
    data = {'app_class': app_class}
    return jsonify(data)


# 读取所有app_class
@app.route('/get_all_app_class', methods={'POST', 'GET'})
def get_all_app_class():
    app_classes = find_all_app_class(t_app_class)
    app_classes = get_id_str(app_classes)
    data = {'app_classes': app_classes}
    return jsonify(data)


# 保存app_instance
@app.route('/save_app_instance', methods={'POST', 'GET'})
def save_app_instance():
    app_class_id = request.values.get("app_class_id")
    user_id = request.values.get("user_id")
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    app_instance = {"app_class_id": ObjectId(app_class_id), "user_id": user_id, "create_time": create_time}
    # 创建应用实例
    app_instance_id = insert_app_instance(t_app_instance, app_instance)
    # 获取执行资源
    executor_resource_ids = get_resource_ids_by_app_class_id(t_app_class, app_class_id, "activityelement")
    # 获取输入资源
    input_resource_ids = get_resource_ids_by_app_class_id(t_app_class, app_class_id, "input")
    # 获取输出资源
    output_resource_ids = get_resource_ids_by_app_class_id(t_app_class, app_class_id, "output")
    # 所有需要的资源,可能需要应用初始时实例化,也有可能是在应用执行过程中产生绑定实例
    all_need_resource_ids = executor_resource_ids.union(input_resource_ids)
    # 初始资源实例化
    for resource_id in all_need_resource_ids:
        if resource_id in output_resource_ids:
            # 对于执行才产生的实例暂时先不绑定
            continue
        else:
            # 对于非执行产生的实例,在初始时进行实例化绑定
            resource_instance_id = get_resource_instance_id(user_id, str(app_instance_id), resource_id)
            insert_app_instance_resource(t_app_instance, app_instance_id, resource_id[1], resource_instance_id)


    # 调用执行引擎
    cf = Coffee_Flow()
    cf.run_predefined_flow()

    return str(app_instance_id)


# 删除app_instance

# 修改app_instance

# 查询app_instance
@app.route('/get_all_app_instance_introduction', methods={'POST', 'GET'})
def get_all_app_instance_introduction():
    app_instance_introduction = find_all_app_instance_introduction(t_app_instance)
    app_instance_introduction = get_id_str(app_instance_introduction)
    data = {'app_classes_introduction': app_instance_introduction}
    return jsonify(data)


@app.route('/get_app_class_by_instance_id', methods={'POST', 'GET'})
def get_app_class_by_instance_id():
    app_instance_id = request.values.get("app_instance_id")
    app_class = find_app_class_by_instance_id(t_app_instance, app_instance_id)
    app_class = get_id_str(app_class)
    data = {'app_class': app_class}
    return jsonify(data)


@app.route('/get_app_instance_action_state_by_instance_id', methods={'POST', 'GET'})
def get_app_instance_action_state_by_instance_id():
    app_instance_id = request.values.get("app_instance_id")
    app_instance_action_state = find_app_instance_action_state_by_instance_id(t_app_instance, app_instance_id)
    app_instance_action_state = get_id_str(app_instance_action_state)
    data = {'app_instance_action_state': app_instance_action_state}
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
