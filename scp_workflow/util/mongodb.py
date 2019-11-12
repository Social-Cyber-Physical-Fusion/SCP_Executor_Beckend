<<<<<<< HEAD
# -*-coding:utf8-*-


def get_id_str(apps):
    if isinstance(apps, dict):
        apps["_id"] = str(apps["_id"])
    else:
        for app in apps:
            app["_id"] = str(app["_id"])
    return apps
=======
# -*-coding:utf8-*-


def get_id_str(apps):
    if isinstance(apps, dict):
        apps["_id"] = str(apps["_id"])
    else:
        for app in apps:
            app["_id"] = str(app["_id"])
    return apps


>>>>>>> c8b65fd34448cf6cf0727b1163f62945c5cf2329
