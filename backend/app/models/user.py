from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
  __tablename__ = 'users'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key= True)
  username = db.Column(db.String(40), nullable=False, unique=True)
  hashed_password = db.Column(db.String(255), nullable=False)
  first_name = db.Column(db.String(25), nullable=False)
  last_name = db.Column(db.String(25), nullable=False)
  middle_initial = db.Column(db.String(1), nullable=True)
  email = db.Column(db.String(255), nullable=False, unique=True)
  phone_number = db.Column(db.String(10), nullable=False, unique=True)
  profile_pic = db.Column(db.String(255), nullable=True)
  address = db.Column(db.String(255), nullable = True )
  birthday = db.Column(db.DateTime, nullable = False)

  specialist_user = db.relationship('Specialist', back_populates='user_specialist', cascade='all, delete')
  transaction_user = db.relationship('Transaction', back_populates="user_transaction", cascade='all, delete')
  booking_user = db.relationship('Booking', back_populates="user_booking", cascade='all, delete')
  favorite_user = db.relationship('Favorite', back_populates="user_favorites", cascade='all, delete')

  @property
  def password(self):
      return self.hashed_password

  @password.setter
  def password(self, password):
      self.hashed_password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)

  def check_phone_number(sel, phone_number):
     return phone_number.isnumeric()

  def to_dict(self):
     return {
         'id': self.id,
         'username': self.username,
         'email': self.email,
         'profile_pic' : self.profile_pic,
         'address' : self.address,
         'birthday' : self.birthday
     }
