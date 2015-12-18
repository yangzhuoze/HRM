# -*- coding: utf-i -*-

from sqlalchemy import Columnt, Integer, String, Date, Text, Datetime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key = True)
    name = Column(String(45), nullable = False)
    companies = relationship('Companies', backref = 'parent')

class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key = True)
    name = Column(String(45), nullable = False)
    parent_id = Column(Integer, ForeignKey('group.id'))
    departments = relationship('Department', backref = 'parent')

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key = True)
    name = Column(String(45), nullable = False)
    parent_id = Column(Integer, ForeignKey('department.id'))
    clerks = relationship('Department', backref = 'department')

class PositionCat(Base):
    __tablename__ = 'positioncat'

    id = Column(Integer, primary_key = True)
    name = Column(String(45), nullable = False)
    position = relationship('Category', backref = 'category')

class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer, primary_key = True)
    name = Column(String(45), nullable = False)
    category_id = Column(Integer, ForeignKey('positioncat.id'))

class PositionTitle(Base):
    __tablename__ = 'positiontitle'

    id = Column(Integer, primary_key = True)
    name = Column(String(45), nullable = False)
    positiontitle = relationship('PositionTitle', backref = 'positiontitle')

class Clerk(Base):
    __tablename__ = 'clerk'

    id = Column(Integer, primary_key = True)
    recordid = Column(String(12), nullable = False, unique = True)
    department_id = Column(Integer, nullable = False, ForeignKey('department.id'))
    position_id = Column(Integer, nullable = False, ForeignKey('position.id'))
    positiontitle_id = Column(Integer, nullable = False, ForeignKey('positiontitle.id'))
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
    salary = Column(Integer, nullable = False)
    openingbank = Column(String(45))
    account = Column(String(20))
    speciality = Column(String(45))
    hobby = Column(String(45))
    vitae = Column(Text())
    relationship = Column(Text())
    remarks = Column(Text())
    booker = Column(Integer)
    booktime = Column(Datetime())
    avatar = Column(String(45), unique = True)
    confirm = Column(Boolean())

