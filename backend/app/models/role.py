from .db import db, environment, SCHEMA

class Role(db.Model):
  __tablename__ = 'roles'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key= True)
  name = db.Column(db.String(12), nullable = False, unique = True)
  description = db.Column(db.String(255), nullable=False)

  specialist_role = db.relationship('Specialist', back_populates='role_specialist', cascade='all, delete')
  def to_dict(self):
     return {
         'id': self.id,
         'name': self.name,
         'description': self.description
     }
