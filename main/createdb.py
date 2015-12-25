from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Models import Base, Group, Company, Department

engine = create_engine('mysql+mysqlconnector://root:joze@localhost:3306/hrm')
DBSession = sessionmaker(bind = engine)
#Base.metadata.create_all(engine)
#print('create success')

session = DBSession()
#group = session.query(Group).filter_by(id = 1).first()
#company = Company(id = 1,  name = 'testCompany', parent = group)
#company2 = Company(id = 2,  name = 'company2',  parent = group)
#session.add(company)
#session.add(company2)
#session.commit()
#
#group2 = session.query(Group).filter_by(id = 2).first()
#company3 = Company(id = 3,  name = 'testCompany33', parent = group2)
#company4 = Company(id = 4,  name = 'company44',  parent = group2)
#session.add(company3)
#session.add(company4)
#session.commit()
#
#group3 = session.query(Group).filter_by(id = 3).first()
#company5 = Company(id = 5,  name = 'testCompany555', parent = group3)
#company6 = Company(id = 6,  name = 'company666',  parent = group3)
#session.add(company5)
#session.add(company6)
#session.commit()

company = session.query(Company).filter_by(id = 1).first()
department1 = Department(id = 1, name = 'testDepartment', parent = company)
department2 = Department(id = 2, name = 'testDepartment22', parent = company)
session.add(department1)
session.add(department2)
company4 = session.query(Company).filter_by(id = 4).first()
department3 = Department(id = 3, name = 'testDepartment3', parent = company4)
department4 = Department(id = 4, name = 'testDepartment4', parent = company4)
session.add(department3)
session.add(department4)
company5 = session.query(Company).filter_by(id = 5).first()
department5 = Department(id = 5, name = 'testDepartment5', parent = company5)
department6 = Department(id = 6, name = 'testDepartment6', parent = company5)
session.add(department5)
session.add(department6)
session.commit()

session.close()
print('success')
