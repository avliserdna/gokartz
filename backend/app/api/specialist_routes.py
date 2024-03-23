from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
from app.models import Specialist, db
from app.forms import SpecialistForm

specialist_routes = Blueprint('specialists', __name__)

@specialist_routes.route('/')
def specialists():
  specialists = Specialist.query.all()
  return {specialist.id: specialist.to_dict() for specialist in specialists}

@specialist_routes.route('/<int:id>')
def specialist(id):
  specialist = Specialist.query.id(id)
  return specialist.to_dict()

@specialist_routes.route('/', methods=['POST'])
@login_required
def add_specialist():
  specialist_data = request.json
  new_specialist = Specialist(**specialist_data, user_id = current_user.id)
  db.session.add(new_specialist)
  db.session.commit()
  return new_specialist.to_dict()

@specialist_routes.route('/<int:id>', methods=["PATCH"])
@login_required
def edit_specialist(id):
  form = SpecialistForm()
  specialist = Specialist.query.get(id)
  specialist.biography = form.data["biography"]
  specialist.portfolio = form.data["portfolio"]

  db.sessiom.commit()
  return specialist.to_dict()
