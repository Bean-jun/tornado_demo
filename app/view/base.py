import tornado.web
from app.tools import trueReturn, to_serialize


class BaseViewHandler(tornado.web.RequestHandler):
    """api 基类

    Args:
        tornado (_type_): _description_

    Raises:
        Exception: _description_

    Returns:
        _type_: _description_
    """
    session = None
    class_table = None

    def true_return(self, data=None, msg="success"):
        self.write(trueReturn(data, msg))

    def false_return(self, data=None, msg="failure"):
        self.write(trueReturn(data, msg))

    def data_received(self, chunk):
        pass

    def get_query_args(self, join_str=None):
        dic = dict()
        for k in self.request.query_arguments.keys():
            if join_str:
                value = join_str.join(self.get_query_arguments(k))
            else:
                value = self.get_query_arguments(k)
            dic[k] = value
        return dic

    def get_query_forms(self, join_str=None):
        dic = dict()
        for k in self.request.body_arguments.keys():
            if join_str:
                value = join_str.join(self.get_body_arguments(k))
            else:
                value = self.get_body_arguments(k)
            dic[k] = value
        return dic

    def initialize(self, **kwargs):
        self.session = getattr(self.application, "db")

    def prepare(self):
        raise Exception("please set current handler models")

    def on_finish(self):
        pass

    def get(self):
        response = self.session.query(self.class_table).all()
        c = to_serialize(response)
        return self.true_return(c)

    def post(self):
        instance = self.class_table(**self.get_query_forms(","))
        self.session.add(instance)
        self.session.commit()
        return self.true_return(to_serialize([instance]))

    def put(self):
        dic = self.get_query_forms(",")
        if "id" not in dic:
            return self.false_return()
        id = dic.pop("id")
        instance = self.session.query(self.class_table).filter(self.class_table.id == id).first()
        for k, v in dic.items():
            if hasattr(instance, k):
                setattr(instance, k, v)
        self.session.commit()
        return self.true_return(to_serialize([instance]))

    def delete(self):
        dic = self.get_query_forms(",")
        if "id" not in dic:
            return self.false_return()
        id = dic.pop("id")
        instance = self.session.query(self.class_table).filter(self.class_table.id == id).first()
        self.session.delete(instance)
        self.session.commit()
        return self.true_return()
