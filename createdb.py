from datetime import datetime
from sqlalchemy import create_engine

from main import session
from main.Models import Base, Group, Company, Department, Clerk, Role,\
    PositionCat, Position, PositionTitle
    
engine = create_engine('mysql+mysqlconnector://root:joze@localhost:3306/hrm')

def create_db():
    Base.metadata.create_all(engine)
    print('create success')
    
def create_group():
    group1 = Group(name = 'group1')
    group2 = Group(name = 'group2')
    group3 = Group(name = 'group3')
    session.add(group1)
    session.add(group2)
    session.add(group3)
    session.commit()

#创建公司
def create_company():
    group = session.query(Group).filter_by(id = 1).first()
    company = Company(id = 1,  name = 'testCompany', parent = group)
    company2 = Company(id = 2,  name = 'company2',  parent = group)
    session.add(company)
    session.add(company2)
    session.commit()

    group2 = session.query(Group).filter_by(id = 2).first()
    company3 = Company(id = 3,  name = 'testCompany33', parent = group2)
    company4 = Company(id = 4,  name = 'company44',  parent = group2)
    session.add(company3)
    session.add(company4)
    session.commit()

    group3 = session.query(Group).filter_by(id = 3).first()
    company5 = Company(id = 5,  name = 'testCompany555', parent = group3)
    company6 = Company(id = 6,  name = 'company666',  parent = group3)
    session.add(company5)
    session.add(company6)
    session.commit()

    company = session.query(Company).filter_by(id = 1).first()
    department1 = Department(name = 'testDepartment', parent = company)
    department2 = Department(name = 'testDepartment22', parent = company)
    session.add(department1)
    session.add(department2)
    company4 = session.query(Company).filter_by(id = 4).first()
    department3 = Department(name = 'testDepartment3', parent = company4)
    department4 = Department(name = 'testDepartment4', parent = company4)
    session.add(department3)
    session.add(department4)
    company5 = session.query(Company).filter_by(id = 5).first()
    department5 = Department(name = 'testDepartment5', parent = company5)
    department6 = Department(name = 'testDepartment6', parent = company5)
    session.add(department5)
    session.add(department6)
    session.commit()

#职位
def create_position():
    positioncat = PositionCat(name = '销售2')
    session.add(positioncat)
    session.commit()
    positionCat = session.query(PositionCat).filter_by(id = 1).first()
    position = Position(name = '苦逼sell屎2', category = positionCat)
    session.add(position)
    session.commit()
    positiontitle = PositionTitle(name = '老牌嘴炮王2')
    session.add(positiontitle)
    session.commit()
    
#创建权限和雇员
def create_clerk():
    role = Role(name = 'Administrator', permission = 0xFFFFFF)
    session.add(role)
    session.commit()
    role = session.query(Role).filter_by(id = 1).first()
    group = session.query(Group).filter_by(id = 1).first()
    company = session.query(Company).filter_by(id = 1).first()
    department = session.query(Department).filter_by(id = 1).first()
    position = session.query(Position).filter_by(id = 1).first()
    positiontitle = session.query(PositionTitle).filter_by(id = 1).first()
    clerk = Clerk(recordid = '201501010101', password = '123123',
        group = group, company = company, department = department,
        position = position, positiontitle = positiontitle,
        birthday = datetime.now().strftime('%Y-%m-%d'),
        role = role, name = 'yyyy', gender = '男', nation = '中国', 
        ethnicity = '汉族', faith = '无', politicalstatus = '团员', 
        identification = '110',  education = '12', confirm = 0)
    session.add(clerk)
    session.commit()
    
def insert_all():
    create_group()
    create_company()
    create_position()
    create_clerk()
    print('insert finish')

if __name__ == '__main__':
    create_db()
    insert_all()
