#!/usr/bin/python3
"""Select all states in hbtn_0e_0_usa"""

#import sqlalchemy as sqla
from sqlalchemy import Integer, String, create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#import MySQLdb
from sys import argv


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                            format(argv[1], argv[2], argv[3]),
                            pool_pre_ping=True)
Base = declarative_base()
Base.metadata.create_all(engine)

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String)

Session = sessionmaker(bind=engine)

session = Session()
for state in session.query(State).order_by(State.id).all():
    print("({}, '{}')".format(state.id, state.name))
session.close()
