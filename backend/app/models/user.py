from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
  __tablename__ = 'users'

  if environment == "production":
    __table_args_ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key= True)
  username = db.Column(db.String(40), nullable=False, unique=True)
  hashed_password = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False, unique=True)
  phone_number = db.Column(db.Number(10), nullable=False, unique=True)
  profile_pic = db.Column(db.String(255), nullable=True)
  address = db.Column(db.String(255), nullable = True )
  birthday = db.Column(db.DateTime, nullable = False)


  @property
  def password(self):
      return self.hashed_password

  @password.setter
  def password(self, password):
      self.hashed_password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)

  def to_dict(self):
     return {
         'id': self.id,
         'username': self.username,
         'email': self.email,
         'profile_pic' : self.profile_pic,
         'address' : self.address,
         'birthday' : self.birthday
     }