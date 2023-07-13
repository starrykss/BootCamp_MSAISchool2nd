from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

os.makedirs("db", exist_ok=True)
engine = create_engine('sqlite:///db/user.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)  

    def __init__(self, name):
        self.name = name    

Base.metadata.create_all(engine)