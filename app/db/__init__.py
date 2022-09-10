from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from ..conf import DB_URI

Base = declarative_base()
engine = create_engine(DB_URI, max_overflow=5)
# autocommit设置为True，操作会将当前session对象里面的缓存全部提交，清空缓存，下次查询时，就是从数据库中查询最新数据，而不是先查询缓存
Session = scoped_session(sessionmaker(bind=engine))


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)
