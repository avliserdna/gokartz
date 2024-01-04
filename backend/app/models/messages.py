from .db import db, environment, SCHEMA, add_prefix_for_prod

class Message(db.Model):
  __tablename__ = 'messages'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key= True)
  sender_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
  message = db.Column(db.String(255), nullable=False)

  user_message = db.relationship('User', back_populates='message_user', cascade='all, delete')
  def to_dict(self):
     return {
         'id': self.id,
         'name': self.name,
         'description': self.description
     }
