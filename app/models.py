from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    checked  = db.Column(db.Integer)

    def __repr__(self):
        return '<Item {} >'.format(self.body)