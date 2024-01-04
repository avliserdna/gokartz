from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
import datetime
from faker import Faker

fake = Faker()

# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', first_name=fake.first_name(), last_name=fake.last_name(), profile_pic='image', address="46 Arrowhead Dr.Waterford, MI 48329", birthday=datetime.datetime(2004, 5, 31), phone_number="8309855822")
    sample = User(
        username='Missy', email='Missy@gokartz.io', password='missymoomoo', first_name=fake.first_name(), last_name=fake.last_name(), profile_pic='image', address="8929 Connelly Ville, North Winfred, ND 66437-9853", birthday=datetime.datetime(1993, 7, 23), phone_number="6052159380")
    db.session.add(demo)
    db.session.add(sample)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text('DELETE FROM users'))

    db.session.commit()
