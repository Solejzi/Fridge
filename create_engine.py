from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lejziDB.models import Base

engine = create_engine('sqlite:///food.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)