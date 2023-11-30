from flask.cli import AppGroup
from .users import seed_users, undo_users
# from .characters import seed_characters, undo_characters
# from .comments import seed_comments, undo_comments
# from .maps import seed_maps, undo_maps
# from .posts import seed_posts, undo_posts
# from .postedmaps import seed_posted_maps, undo_posted_maps
# from .profiles import seed_profiles, undo_profiles
# from .teamsuggestions import seed_team_suggestions, undo_team_suggestions
# from .likeDislikes import seed_like_dislikes, undo_like_dislikes

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        # undo_like_dislikes()
        # undo_comments()
        # undo_posted_maps()
        # undo_team_suggestions()
        # undo_profiles()
        # undo_posts()
        # undo_characters()
        # undo_maps()
        undo_users()
    seed_users()
    # seed_maps()
    # seed_characters()
    # seed_posts()
    # seed_profiles()
    # seed_team_suggestions()
    # seed_posted_maps()
    # seed_comments()
    # seed_like_dislikes()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    # undo_like_dislikes()
    # undo_comments()
    # undo_posted_maps()
    # undo_team_suggestions()
    # undo_profiles()
    # undo_posts()
    # undo_characters()
    # undo_maps()
    undo_users()
    # Add other undo functions here
