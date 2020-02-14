from application import db


class Cooler (db.Model):
    __tablename__ = 'cooler'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Integer, db.ForeignKey('items.id'))
    is_good = db.Column(db.Boolean)
    item_opened = db.Column(db.Boolean)

    items = db.relationship('Items', back_populates='cooler')

    def __repr__(self):
        return f'Im a Cooler'


class Fridge (db.Model):
    __tablename__ = 'fridge'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Integer, db.ForeignKey('items.id'))
    item_opened = db.Column(db.Boolean)
    is_good = db.Column(db.Boolean)

    items = db.relationship('Items', back_populates='cooler')

    def __repr__(self):
        return f'Im a Fridge'


class ItemsCategories(db.Model):
    __tablename__ = 'itemsCategories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    items = db.relationship('Items', back_populates='itemsCategories')


class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    expired_opened = db.Column(db.Integer)
    use_by = db.Column(db.DateTime)
    do_i_need_it = db.Column(db.Integer)
    category = db.Column(db.Integer, db.ForeignKey('itemsCategories.id'))
    itemCategories = db.relationship('ItemCategories', back_populates='items')
    fridge = db.relationship('Fridge', back_populates='items')
    cooler = db.relationship('Cooler', back_populates='items')

