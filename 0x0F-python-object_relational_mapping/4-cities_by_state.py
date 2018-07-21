#!/usr/bin/python3
"""List all states using mysqldb"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities"
                " JOIN states ON states.id=cities.state_id ORDER BY cities.id")
    for row in cur.fetchall():
        print("({}, '{}', '{}')".format(row[0], row[1], row[2]))
