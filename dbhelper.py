#!/bin/python3

__all__ = ['DBSession','Picture','Tag']

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = json.load(open('dbconfig.json'))
engine = create_engine('{dbconnector}://{user}:{password}@{host}:{port}/{database}?charset=utf8'.format(**config),
        encoding='utf-8', echo=False)
DBSession = sessionmaker(bind=engine)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, INT, BLOB, BINARY
Base = declarative_base()

class Picture(Base):
    __tablename__ = 'picture'
    _id = Column(INT, primary_key=True)
    size_width = Column(INT)
    size_height = Column(INT)
    tags = Column(VARCHAR(8000))
    score = Column(INT)
    url = Column(VARCHAR(8000))
    preview = Column(BINARY)
    rating = Column(VARCHAR(255))
    user = Column(VARCHAR(255))

    def __str__(self):
        return '({_id},{rating},{score},{size_width},{size_height},{tags},{url},{user},{preview})'.format(
                _id=self._id,rating=self.rating,score=self.score,size_width=self.size_width,size_height=self.size_height,
                tags=self.tags,url=self.url,user=self.user,preview=type(self.preview))

class Tag(Base):
    __tablename__ = 'tag'
    _id = Column(INT, primary_key=True)
    name = Column(VARCHAR(255))
