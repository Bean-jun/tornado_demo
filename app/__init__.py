import tornado.web

from app.db import Session, init_db
from app.db.models import *


class Application(tornado.web.Application):

    def __init__(self, handlers=None, default_host=None, transforms=None, **settings):
        super().__init__(handlers=handlers, default_host=default_host, transforms=transforms, **settings)
        self.db = Session()


def create_app():
    init_db()

    from app.view import handlers
    app = Application(handlers)

    return app
