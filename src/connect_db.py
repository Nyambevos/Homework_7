from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:pwd12345678@localhost:5432/postgres")
Session = sessionmaker(bind=engine)
session = Session()