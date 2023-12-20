from config.db import meta , engine # Import your SQLAlchemy engine
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Define your table
from sqlalchemy import Table, Column, Integer, String

students = Table(
    'students',meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('country', String(255))
)

# Create the table in the database
meta.create_all(bind=engine)


# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add data to the table
new_student = students.insert().values(name='John Doe', email='john@example.com', country='USA')
session.execute(new_student)

# Commit the changes
session.commit()

# Close the session
session.close()
