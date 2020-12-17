from db import db


class ItemModel(db.Model): #extends db.Model
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) #foreignkey is aa reference to a coloumn from another db table
    store = db.relationship('StoreModel') #sets the relationship to the StoreModel class

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() ### .query is a query builder from the db module which creates a sql statement such as "SELECT *" the filter method appends a "WHERE' clause based on the key/values passed.

    def save_to_db(self):   #updates or inserts data into the database
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
