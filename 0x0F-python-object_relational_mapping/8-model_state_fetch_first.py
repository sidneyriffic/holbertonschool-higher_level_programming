#!/usr/bin/python3
"""Fetch all states using sqlalchemy"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).first()
    if row:
        print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")
