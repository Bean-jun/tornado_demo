import os

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# service
DEBUG = True
HOST = "0.0.0.0"
PORT = "8888"

# database
DB_USER = "root"
DB_PASSWORD = "0009"
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_DB = "TornadoBlog"
DB_URI = "mysql+pymysql://%s:%s@%s:%s/%s" % (DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DB)
