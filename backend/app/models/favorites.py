from .db import db, environment, SCHEMA, add_prefix_for_prod


class Favorite(db.Model):
  __tablename__ = 'favorites'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key= True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
  specialist_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("specialists.id")), nullable=False)

  user_favorites =db.relationship('User', back_populates='favorite_user', cascade='all, delete')
  specialist_favorites = db.relationship('Specialist', back_populates='favorite_specialist', cascade='all, delete')
  def to_dict(self):
     return {
         'id': self.id,
         'user_id': self.user_id,
         'specialist_id': self.specialist_id     }
