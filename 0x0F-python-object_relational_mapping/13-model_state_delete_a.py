#!/usr/bin/python3
"""Fetch all states using sqlalchemy"""


from model_state import Base, State
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
    qry = session.query(State).filter(State.name.contains(func.binary("a")))
    for record in qry.all():
        session.delete(record)
    session.commit()
