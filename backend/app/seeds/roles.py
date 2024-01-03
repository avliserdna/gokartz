from app.models import db, Role, environment, SCHEMA
from sqlalchemy.sql import text
from faker import Faker

fake = Faker()

# Adds a demo user, you can add other users here if you want
def seed_roles():
    videographer = Role(
        name="Videographer",
        description=fake.text()
        )
    barber = Role(
        name="Barber",
        description=fake.text()
        )
    graphic_designer = Role(
        name="Graphic Designer",
        description=fake.text()
    )
    db.session.add(videographer)
    db.session.add(barber)
    db.session.add(graphic_designer)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_roles():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.roles RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM roles"))

    db.session.commit()
