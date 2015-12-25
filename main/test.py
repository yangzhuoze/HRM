from Models import Group, Company, Department
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:joze@localhost:3306/hrm')
DBSession = sessionmaker(bind = engine)
session = DBSession()

for i in range(3):
    group = Group(id = i + 3, name = 'group%s' % (str)(i + 2))
    session.add(group)

for i in session.query(Group).all():
    print('id:%s, name:%s' % (i.id, i.name))