<<<<<<< HEAD
# -*-coding:utf8-*-
from bson import ObjectId

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


def find_app_class_by_id(t_app_class, app_class_id):
    app_class = t_app_class.find_one({'_id': ObjectId(app_class_id)})
    return app_class


def get_resource_ids_by_app_class_id(t_app_class, app_class_id, type):
    app_class = t_app_class.find_one({'_id': ObjectId(app_class_id)})
    resource_ids = set()
    for childShape in app_class['childShapes']:
        if type in childShape['properties']:
            # todo 会有多个资源,要分开获取
            resource_ids.add(childShape['properties'][type])
    resource_ids.add("咖啡机1")
    return resource_ids


def gete_input_resource_ids_by_app_class_id(t_app_class, app_class_id):
    app_class = t_app_class.find_one({'_id': ObjectId(app_class_id)})
    resource_ids = set()
    for childShape in app_class['childShapes']:
        if 'servicetaskclass' in childShape['properties']:
            resource_ids.add(childShape['properties']['name'])
    return resource_ids


def get_output_resource_ids_by_app_class_id(t_app_class, app_class_id):
    app_class = t_app_class.find_one({'_id': ObjectId(app_class_id)})
    resource_ids = set()
    for childShape in app_class['childShapes']:
        if 'servicetaskclass' in childShape['properties']:
            resource_ids.add(childShape['properties']['name'])
    return resource_ids


"""t_app_instance
"""


def insert_app_instance(t_app_instance, app_instance):
    insert_one_result = t_app_instance.insert_one(app_instance)
    return insert_one_result.inserted_id


# 课题四接口服务
def get_resource_instance_id(user_id, app_instance_id, resource_id):
    return 0


def insert_app_instance_resource(t_app_instance, app_instance_id, resource_id, resource_instance_id):
    myquery = {"_id": app_instance_id}
    newvalues = {"$set": {"resource." + resource_id: resource_instance_id}}
    t_app_instance.update_one(myquery, newvalues)
=======
# -*-coding:utf8-*-
from bson import ObjectId

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


def find_app_class_by_id(t_app_class, app_class_id):
    app_class = t_app_class.find_one({'_id': ObjectId(app_class_id)})
    return app_class


def get_resource_ids_by_app_class_id(t_app_class, app_class_id, type):
    app_class = t_app_class.find_one({'_id': ObjectId(app_class_id)})
    resource_ids = set()
    for childShape in app_class['childShapes']:
        if type in childShape['properties']:
            # todo 会有多个资源,要分开获取
            result = childShape['properties'][type]
            if type == "activityelement":
                resource_ids.add((result['type'], result['id']))
            else:
                resource_ids.add(('云应用', 'sid-45939CC7-EAED-404F-8DCD-6409A512403E'))
    return resource_ids


def gete_input_resource_ids_by_app_class_id(t_app_class, app_class_id):
    app_class = t_app_class.find_one({'_id': ObjectId(app_class_id)})
    resource_ids = set()
    for childShape in app_class['childShapes']:
        if 'servicetaskclass' in childShape['properties']:
            resource_ids.add(childShape['properties']['name'])
    return resource_ids


def get_output_resource_ids_by_app_class_id(t_app_class, app_class_id):
    app_class = t_app_class.find_one({'_id': ObjectId(app_class_id)})
    resource_ids = set()
    for childShape in app_class['childShapes']:
        if 'servicetaskclass' in childShape['properties']:
            resource_ids.add(childShape['properties']['name'])
    return resource_ids


"""t_app_instance
"""


def insert_app_instance(t_app_instance, app_instance):
    insert_one_result = t_app_instance.insert_one(app_instance)
    return insert_one_result.inserted_id


# 课题四接口服务
def get_resource_instance_id(user_id, app_instance_id, resource_id):
    return 0


def insert_app_instance_resource(t_app_instance, app_instance_id, resource_id, resource_instance_id):
    myquery = {"_id": app_instance_id}
    newvalues = {"$set": {"resource." + resource_id: resource_instance_id}}
    t_app_instance.update_one(myquery, newvalues)


def find_all_app_instance_introduction(t_app_instance):
    app_instance_introduction = []
    result = t_app_instance.aggregate([
        {
            "$lookup": {
                "from": "t_app_class",
                "localField": "app_class_id",
                "foreignField": "_id",
                "as": "app_class"
            }
        },
        {
            "$unwind": "$app_class"
        },
        {
            "$project": {
                "_id": 1,
                "user_id": 1,
                "create_time": 1,
                "app_class.properties.name": 1
            }
        }
    ])
    for app_instance in result:
        app_instance_introduction.append(app_instance)
    return app_instance_introduction


def find_app_class_by_instance_id(t_app_instance, app_instance_id):
    app_class = []
    result = t_app_instance.aggregate([
        {
            "$lookup": {
                "from": "t_app_class",
                "localField": "app_class_id",
                "foreignField": "_id",
                "as": "app_class"
            }
        },
        {
            "$unwind": "$app_class"
        },
        {
            "$project": {
                "_id": 1,
                "app_class.childShapes": 1
            }
        },
        {
            "$match": {
                "_id": ObjectId(app_instance_id)
            }
        }
    ])
    for app_instance in result:
        app_class.append(app_instance)
    return app_class[0]


def find_app_instance_action_state_by_instance_id(t_app_instance, app_instance_id):
    app_instance_action_state = t_app_instance.find_one({'_id': ObjectId(app_instance_id)}, {"action_state": 1})
    return app_instance_action_state
>>>>>>> c8b65fd34448cf6cf0727b1163f62945c5cf2329
