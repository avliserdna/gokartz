from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import User, db

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()

# Edit user info NEEDS PROPER AUTH, may reconsider to move to auth routes
@user_routes.route('/<int:id>', methods=['PUT'])
@login_required
def edit_user(id):
    form = request.json
    edited_user = User(id = id, **form)
    db.session.add(edited_user)
    db.session.commit()

    return edited_user.to_dict()

@user_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    # May need to log out user here
    return {"message": "user succesfully deleted"}
