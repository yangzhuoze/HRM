from Models import Group
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:joze@localhost:3306/hrm')
DBSession = sessionmaker(bind = engine)
session = DBSession()

print(session.query(Group).filter_by(id = 1).first().name)
session.close()