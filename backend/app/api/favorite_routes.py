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

@favorite_routes.route('/<int:id>')
@login_required
def favorites(id):
  """
    Query for a favorite by id and returns that favorite in a dictionary
  """
  favorite = Favorite.query.get(id)
  return favorite.to_dict()

@favorite_routes.route('/')
@login_required
def post_favorites():
    favorites_data = request.json
    new_favorite = Favorite(**favorites_data, user_id = current_user.id)
    db.session.add(new_favorite)
    db.session.commit()

    return new_favorite.to_dict()

@favorite_routes.route('/<int:id>', methods=['PUT'])
@login_required
def updated_favorite(id):
   form = FavoriteForm()
   favorite = Favorite.query.get(id)

   favorite.user_id = form.data['user_id']
   favorite.specialist_id = form.data['specialist_id']

   db.session.commit()

   return favorite.to_dict()
