from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Models import Base

engine = create_engine('mysql+mysqlconnector://root:joze@localhost:3306/hrm')
DBSession = sessionmaker(bind = engine)
Base.metadata.create_all(engine)
print('create success')