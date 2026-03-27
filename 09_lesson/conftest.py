from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

db_connection_string = "postgresql://postgres:1111@localhost:5434/lesson"
db = create_engine(db_connection_string)

engine = create_engine(db_connection_string)
Session = sessionmaker(bind=engine)
metadata = MetaData()

students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)
