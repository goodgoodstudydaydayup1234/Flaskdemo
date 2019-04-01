"""
ORM:O用于生成数据库中表
"""


# class Book():
#     id = None
#     name = None
#     price = None
#
#     def __str__(self):
#         return "%s  %s  %s" % (self.id, self.name, self.price)


from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb1",
                                    encoding='utf8', echo=True)

from  sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)

from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)


if __name__ == "__main__":
    # 创建表，必须写在main模块
    Base.metadata.create_all(bind=engine)
