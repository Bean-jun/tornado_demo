import datetime


# 时间相关
def date2str(date):
    return date.strftime("%Y-%m-%d")


def datetime2str(date_time):
    return date_time.strftime("%Y-%m-%d %H:%M:%S")


def time2str_factory(date):
    if isinstance(date, datetime.datetime):
        return datetime2str(date)
    if isinstance(date, datetime.date):
        return date2str(date)
    return date


def cure_time(dic):
    assert isinstance(dic, dict)
    response = dict()
    for k, v in dic.items():
        response[k] = time2str_factory(v)
    return response


# 序列化相关
def to_dict_me(obj):
    dic = {}

    for column in obj.__table__.columns:
        dic[column.name] = getattr(obj, column.name)

    return dic


def list_2_to_dict_me(objs):
    response = []
    if isinstance(objs, (tuple, list)):
        for obj in objs:
            response.append(to_dict_me(obj))
    else:
        response.append(to_dict_me(objs))
    return response


def to_serialize(objs):
    if isinstance(objs, (tuple, list)):
        result = list_2_to_dict_me(objs)
        response = []
        for dic in result:
            response.append(cure_time(dic))
        return response
    return objs


# 响应相关
def trueReturn(data, msg="success"):
    return {
        "status": True,
        "data": data,
        "msg": msg
    }


def falseReturn(data, msg='failure'):
    return {
        "status": False,
        "data": data,
        "msg": msg
    }
