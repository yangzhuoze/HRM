# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Date, Text, DateTime, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key = True)
    name = Column(String(45), nullable = False, unique = True)
    companies = relationship('Company', backref = 'parent')

class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key = True)
    name = Column(String(45), nullable = False)
    parent_id = Column(Integer, ForeignKey('group.id'))
    departments = relationship('Department', backref = 'parent')

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    parent_id = Column(Integer, ForeignKey('company.id'))
    clerks = relationship('Clerk', backref = 'department')

class PositionCat(Base):
    __tablename__ = 'positioncat'

    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False, unique = True)
    position = relationship('Position', backref = 'category')

class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False, unique = True)
    category_id = Column(Integer, ForeignKey('positioncat.id'))
    clerks = relationship('Clerk', backref = 'position')

class PositionTitle(Base):
    __tablename__ = 'positiontitle'

    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False, unique = True)
    positiontitle = relationship('Clerk', backref = 'positiontitle')

class Salary(Base):
    __tablename__ = 'salary'

    id = Column(Integer, primary_key = True)
    name = Column(String(45), nullable = False)
    booker_id = Column(Integer, ForeignKey('clerk.id'))
    item = relationship('SalaryItemCost', backref = 'salary')
    booktime = Column(Date(), nullable = False)
    confirm = Column(Boolean(), nullable = False, default = False)

class SalaryItem(Base):
    __tablename__ = 'salaryitem'

    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False)
    salary = relationship('SalaryItemCost', backref = 'item')

class SalaryItemCost(Base):
    __tablename__ = 'salaryitemcost'

    id = Column(Integer, primary_key = True)
    salary_id = Column(Integer, ForeignKey('salary.id'))
    item_id = Column(Integer, ForeignKey('salaryitem.id'))
    cost = Column(Numeric(precision = 2), nullable = False)
    clerks = relationship('Clerk', backref = 'salary')

class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key = True)
    name = Column(String(20), nullable = False, unique = True)
    permission = Column(Integer, nullable = False)
    clerks = relationship('Clerk', backref = 'role')

class Clerk(Base):
    __tablename__ = 'clerk'

    id = Column(Integer, primary_key = True)
    recordid = Column(String(12), nullable = False, unique = True)
    password = Column(String(20),  nullable = False)
    department_id = Column(Integer, ForeignKey('department.id'))
    position_id = Column(Integer, ForeignKey('position.id'))
    positiontitle_id = Column(Integer, ForeignKey('positiontitle.id'))
    role_id = Column(Integer, ForeignKey('role.id'))
    salary_book = relationship('Salary', backref = 'booker')
    name = Column(String(45), nullable = False)
    gender = Column(String(2), nullable = False)
    email = Column(String(45))
    phone = Column(String(15))
    qq = Column(String(10))
    mobilephone = Column(String(15))
    address = Column(String(45))
    postcode = Column(Integer)
    nation = Column(String(20), nullable = False)
    birthplace = Column(String(30))
    birthday = Column(Date())
    ethnicity = Column(String(30), nullable = False)
    faith = Column(String(30), nullable = False)
    politicalstatur = Column(String(20), nullable = False)
    identification = Column(String(18), nullable = False)
    socialsecurity = Column(String(30))
    education = Column(String(10), nullable = False)
    educationtime = Column(Integer)
    major = Column(String(20))
    salary_id = Column(Integer, ForeignKey('salaryitemcost.id'))
    openingbank = Column(String(45))
    account = Column(String(20))
    speciality = Column(String(45))
    hobby = Column(String(45))
    vitae = Column(Text())
    relationship = Column(Text())
    remarks = Column(Text())
    booker = Column(Integer)
    booktime = Column(DateTime())
    avatar = Column(String(45), unique = True)
    confirm = Column(Boolean(), nullable = False, default = False)
