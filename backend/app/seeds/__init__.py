from flask.cli import AppGroup
from .users import seed_users, undo_users
from .roles import seed_roles, undo_roles
from .specialists import seed_specialists, undo_specialists
from .transactions import seed_transactions, undo_transactions
from .bookings import seed_bookings, undo_bookings
from .favorites import seed_favorites, undo_favorites
from .messages import seed_messages, undo_messages

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
        undo_transactions()
        undo_specialists()
        undo_users()
        undo_roles()
        undo_bookings()
        undo_favorites()
        undo_messages()


    seed_users()
    seed_roles()
    seed_specialists()
    seed_transactions()
    seed_bookings()
    seed_favorites()
    seed_messages()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_roles()
    undo_specialists()
    undo_transactions()
    undo_users()
    undo_bookings()
    undo_favorites()
    undo_messages()
    # Add other undo functions here
