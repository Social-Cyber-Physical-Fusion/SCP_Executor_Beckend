# -*-coding:utf8-*-
from flask import make_response

"""t_app_class
"""


def insert_app_class(t_app_class, app_class):
    insert_one_result = t_app_class.insert_one(app_class)
    return insert_one_result.inserted_id


def find_all_app_class_introduction(t_app_class):
    app_classes_introduction = []
    for app_class in t_app_class.find({}, {"properties": 1}):
        app_classes_introduction.append(app_class)
    return app_classes_introduction


def find_all_app_class(t_app_class):
    app_classes = []
    for app_class in t_app_class.find():
        app_classes.append(app_class)
    return app_classes


"""t_app_instance
"""


def insert_app_instance(t_app_instance, app_instance):
    insert_one_result = t_app_instance.insert_one(app_instance)
    return insert_one_result.inserted_id
