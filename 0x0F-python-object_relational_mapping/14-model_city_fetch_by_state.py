#!/usr/bin/python3
"""Fetch cities by state"""


from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy import func
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    qry = session.query(State, City).filter(State.id == City.state_id)
    for record in qry.all():
        print("{}: ({}) {}".format(record.State.name, record.City.id,
                                   record.City.name))
