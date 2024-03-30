from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
from app.models import Favorite, db
from app.forms import FavoriteForm

favorite_routes = Blueprint('favorites', __name__)

@favorite_routes.route('/')
@login_required
def favorites():
  """
    Query for all favorites and returns them in a list of user dictionaries
  """
  favorites = Favorite.query.all()
  return {'favorites': [favorite.to_dict() for favorite in favorites]}
