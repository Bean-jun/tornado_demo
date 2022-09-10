from app.view.base import BaseViewHandler
from app.db.models import *


class ExampleViewHandler(BaseViewHandler):
    """示例api

    Args:
        BaseViewHandler (_type_): _description_
    """

    def prepare(self):
        self.class_table = None

    def get(self):
        response = self.get_query_args()
        self.true_return(response)

    def post(self):
        response = self.get_query_forms()
        self.true_return(response)

    def put(self):
        response = self.get_query_forms()
        self.true_return(response)

    def delete(self):
        response = self.get_query_forms()
        self.true_return(response)
