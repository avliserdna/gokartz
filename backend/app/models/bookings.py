from .db import db, environment, SCHEMA, add_prefix_for_prod


class Booking(db.Model):
  __tablename__ = 'bookings'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key= True)
  user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
  specialist_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("specialists.id")), nullable=False)
  appointed_day = db.Column(db.Date(), nullable=False)
  appointed_time = db.Column(db.String(), nullable=False)

  specialist_booking = db.relationship('Specialist', back_populates='booking_specialist', cascade='all, delete')
  user_booking = db.relationship('User', back_populates='booking_user', cascade='all, delete')

  def to_dict(self):
     return {
         'id': self.id,
         'user_id': self.user_id,
         'specialist_id': self.specialist_id,
         'appointed_day': self.appointed_day,
         'appointed_time': self.appointed_time
     }
