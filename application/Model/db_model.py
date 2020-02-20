from application import db


class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String, unique=True, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    fridge_id = db.Column(db.Integer, db.ForeignKey('fridge.id'))
    fridge = db.relationship('Fridge', back_populates='user')


class Fridge(db.Model):
    __tablename__ = 'fridge'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user = db.relationship('User', back_populates='fridge')
    in_fridge = db.relationship('InFridge', back_populates='fridge')



class InFridge(db.Model):
    __tablename__ = 'inFridge'
    id = db.Column(db.Integer, primary_key=True)
    fridge_id = db.Column(db.Integer, db.ForeignKey('fridge.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    quantity = db.Column(db.Integer)
    expired_date = db.Column(db.DateTime)
    items = db.relationship('Items', back_populates='inFridge')
    fridge = db.relationship('Fridge', back_populates='inFridge')
    openedItem = db.relationship('OpenItem', back_populates='inFridge')


class Items(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    expired_opened = db.Column(db.Integer)
    do_i_need_it = db.Column(db.Integer)
    category = db.Column(db.Integer, db.ForeignKey('itemsCategories.id'))
    itemCategories = db.relationship('ItemCategories', back_populates='items')
    openedItem = db.relationship('OpenedItem', back_populates='items')
    in_fridge = db.relationship('InFridge', back_populates='items')


class OpenedItem(db.Model):
    __tablename__ = 'openedItem'
    id = db.Column(db.Integer, primary_key=True)
    fridge_id = db.Column(db.Integer, db.ForeignKey('fridge.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    when = db.Column(db.DateTime)
    item = db.relationship('Item', back_populates='openedItem')
    in_fridge = db.relationship('InFridge', back_populates='openedItem')


class ItemsCategories(db.Model):
    __tablename__ = 'itemsCategories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    items = db.relationship('Items', back_populates='itemsCategories')
