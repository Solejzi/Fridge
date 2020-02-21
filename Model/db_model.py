from application import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    fridge_id = db.Column(db.Integer, db.ForeignKey('fridge.id'))
    fridge = db.relationship('Fridge', back_populates='users')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Fridge(db.Model):
    __tablename__ = 'fridge'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    users = db.relationship('Users', back_populates='fridge')

    inFridge = db.relationship('InFridge', back_populates='fridge')
    openedItem = db.relationship('OpenedItem', back_populates='fridge')


class InFridge(db.Model):
    __tablename__ = 'inFridge'
    id = db.Column(db.Integer, primary_key=True)
    fridge_id = db.Column(db.Integer, db.ForeignKey('fridge.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    quantity = db.Column(db.Integer)
    expired_date = db.Column(db.DateTime)
    opened = db.Column(db.Integer)

    fridge = db.relationship('Fridge', back_populates='inFridge')
    items = db.relationship('Items', back_populates='inFridge')


class OpenedItem(db.Model):
    __tablename__ = 'openedItem'
    id = db.Column(db.Integer, primary_key=True)
    when = db.Column(db.DateTime)
    fridge_id = db.Column(db.Integer, db.ForeignKey('fridge.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    items = db.relationship('Items', back_populates='openedItem')
    fridge = db.relationship('Fridge', back_populates='openedItem')


class Items(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    expired_opened = db.Column(db.Integer)
    do_i_need_it = db.Column(db.Integer)
    category = db.Column(db.Integer, db.ForeignKey('itemsCategories.id'))
    itemsCategories = db.relationship('ItemsCategories', back_populates='items')
    openedItem = db.relationship('OpenedItem', back_populates='items')
    inFridge = db.relationship('InFridge', back_populates='items')



class ItemsCategories(db.Model):
    __tablename__ = 'itemsCategories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    items = db.relationship('Items', back_populates='itemsCategories')
