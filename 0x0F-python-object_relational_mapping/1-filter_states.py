#!/usr/bin/python3
#Prints all states starting with a capital N
import sys
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id;")
    data = curs.fechall()
    for row in data:
        if row[1].startswith("N"):
            print (row)
    curs.close()
    db.close()
