from app.models import db, Booking, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime, date
from faker import Faker
from faker.providers import date_time

fake = Faker()
fake.add_provider(date_time)
now = datetime.now()
fake_time = now.strftime("%H:%M:%S")
# Adds a demo user, you can add other users here if you want
def seed_bookings():
    demo = Booking(
      user_id=1, specialist_id=1, appointed_day=date.today(), appointed_time=fake_time)
    print(demo)
    db.session.add(demo)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_bookings():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.bookings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM bookings"))

    db.session.commit()
