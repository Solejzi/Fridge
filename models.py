from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cooler(Base):
    __tablename__ = 'cooler'
    id = Column(Integer, primary_key=True)
    item = Column(Integer, ForeignKey('items.name'))

    items_in_cooler = Column(Integer)
    items_closed = Column(Boolean)
    items_opened = Column(Boolean)
    items_missing = Column(Boolean)

    items = relationship('Items', back_populates='cooler')

    def __repr__(self):
        return f'fridge {self.items_total}'


class Fridge(Base):
    __tablename__ = 'fridge'

    id = Column(Integer, primary_key=ForeignKey('items.id'))
    item = Column(Integer, ForeignKey('items.name'))
    items_in_fridge = Column(Integer)
    items_closed = Column(Boolean)
    items_opened = Column(Boolean)

    items = relationship('Items', back_populates='fridge')
    def __init__(self, items_in_fridge, items_closed, items_opened):
        self.items_in_fridge = items_in_fridge
        self.items_closed = items_closed
        self.items_opened = items_opened
    def __repr__(self):
        return f'fridge items:{self.items_total}'


class FoodCategories(Base):
    __tablename__ = 'foodCategories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    items = relationship('Items', back_populates='foodCategories')

    def __init__(self, name):
        self.name = name

class Items(Base):
    __tablename__ = 'items'

    name = Column(String, primary_key=True)
    expired_opened = Column(Integer)
    use_by = Column(Integer)
    do_i_need_it = Column(Integer)
    category = Column(Integer, ForeignKey('foodCategories.id'))
    foodCategories = relationship('FoodCategories', back_populates='items')
    fridge = relationship('Fridge', back_populates='items')
    cooler = relationship('Cooler', back_populates='items')

    def __init__(self, name, expired_opened, use_by, do_i_need_it, category):
        self.name = name
        self.expired_opened = expired_opened
        self.use_by = use_by
        self.do_i_need_it = do_i_need_it
        self.category = category



