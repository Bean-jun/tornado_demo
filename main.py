import os

import tornado.httpserver
import tornado.ioloop

from app import conf
from app import create_app

if __name__ == "__main__":
    app = create_app()
    print("\n start server on: http://127.0.0.1:%s" % conf.PORT)
    if conf.DEBUG:
        app.listen(conf.PORT)
    else:
        httpserver = tornado.httpserver.HTTPServer(app)
        httpserver.bind(conf.PORT, conf.HOST)
        httpserver.start(os.cpu_count() * 2)

    tornado.ioloop.IOLoop.instance().start()
