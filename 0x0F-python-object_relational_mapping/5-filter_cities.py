#!/usr/bin/python3
"""List all states using mysqldb"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities"
                " JOIN states ON states.id=cities.state_id "
                "WHERE states.name=%s COLLATE latin1_general_cs "
                "ORDER BY cities.id", (argv[4],))
    print(", ".join([x[0] for x in cur.fetchall()]))
