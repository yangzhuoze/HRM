import sys

from PyQt5 import QtWidgets
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = QtWidgets.QApplication(sys.argv)
engine = create_engine('mysql+mysqlconnector://root:joze@localhost:3306/hrm')
DBSession = sessionmaker(bind = engine)
session = DBSession()
