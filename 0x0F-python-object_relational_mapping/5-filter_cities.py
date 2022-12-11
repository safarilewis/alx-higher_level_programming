#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument"""
import sys
import MySQLdb
if __name__ == '__main__':
    """Connects to database and gets data"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities
                    JOIN states ON cities.state_id = states.id
                    WHERE states.name LIKE BINARY %s
                    ORDER BY cities.id;""", [sys.argv[4]])
    data = cursor.fetchall()
    l = []
    for row in data:
        l.append(row[0])
        print(", ".join(l))
    cursor.close()
    db.close()
