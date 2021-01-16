from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}

    @classmethod
    def find_item_in_store(cls, name, store_id):
        from models.store import StoreModel
        store = StoreModel.query.filter_by(id=store_id).first()
        if store:
            return store.items.filter_by(name=name).first()

    def save_to_database(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()





### Udemy Section 6
# from db import db

# class ItemModel(db.Model):
    # # SQLAlchemy attributes; look at 'user.py' for the implementation descriptions
    # __tablename__ = 'items'
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(80))
    # price = db.Column(db.Float(precision=2)) # 'precision' limits the number entered to 2 decimal places

    # # relationship with 'stores' table
    # store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) # so we can say which store the item belongs too
    # store = db.relationship('StoreModel') # essentially, this is an SQLAlchemy way of performing a 'JOIN'

    # def __init__(self, name, price, store_id):
        # self.name = name
        # self.price = price
        # self.store_id = store_id

    # def json(self):
        # return {'name': self.name, 'price': self.price}

    # @classmethod
    # def find_by_name(cls, name):
        # return cls.query.filter_by(name=name).first() # does the same thing as 'Item.find_by_name()' from the old code saved in 'item.py - Udemy Section 5'

    # def save_to_database(self):
        # db.session.add(self) # performs an UPDATE query instead of an INSERT so we can now use thos method for both events
        # db.session.commit()

    # def delete_from_database(self):
        # db.session.delete(self)
        # db.session.commit()
