from .db import db, environment, SCHEMA, add_prefix_for_prod


class Transaction(db.Model):
  __tablename__ = 'transactions'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key= True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
  specialist_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("specialists.id")), nullable=False)
  price = db.Column(db.Double(), nullable=False)
  service = db.Column(db.String(255), nullable=True)
  date = db.Column(db.DateTime())

  specialist_transaction = db.relationship('Specialist', back_populates='transaction_specialist', cascade='all, delete')
  user_transaction = db.relationship('User', back_populates='transaction_user', cascade='all, delete')

  def to_dict(self):
     return {
         'id': self.id,
         'user_id': self.user_id,
         'specialist_id': self.specialist_id,
         'price': self.price,
         'service': self.service,
         'date': self.date
     }
