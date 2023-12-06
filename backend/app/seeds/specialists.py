from app.models import db, Specialist, environment, SCHEMA
import datetime
from faker import Faker
from faker.providers import date_time

fake = Faker()
fake.add_provider(date_time)
# Adds a demo user, you can add other users here if you want
def seed_specialists():
    demo = Specialist(
      user_id=1, role_id=3, biography=fake.text(), portfolio=fake.text())
    db.session.add(demo)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_specialists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.specialists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM specialists")

    db.session.commit()
