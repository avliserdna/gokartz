from .db import db, environment, SCHEMA, add_prefix_for_prod

from sqlalchemy.dialects.postgresql import ARRAY

class Specialist(db.Model):
  __tablename__ = 'specialists'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key= True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
  role_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("roles.id")), nullable=False)
  biography = db.Column(db.String(255), nullable=False)
  portfolio = db.Column(db.String(255), nullable=True) # optional portfolio, should be a link

  role_specialist = db.relationship('Role', back_populates='specialist_role')
  user_specialist = db.relationship('User', back_populates='specialist_user')

  def to_dict(self):
     return {
         'id': self.id,
         'user_id': self.user_id,
         'role_id': self.role_id,
        #  'availability': self.availability,
         'biography': self.biography,
         'portfolio': self.portfolio
     }
