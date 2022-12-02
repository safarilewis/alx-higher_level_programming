#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,user=sys.argv[1],password=sys.argv[2],db=sys.argv[3])
    cursor = db.cursor();
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close