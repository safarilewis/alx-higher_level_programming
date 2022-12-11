#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument"""
import sys
import MySQLdb
if __name__ == '__main__':
    """Connects to database and gets data"""
    db = MySQLdb.connect(host="localhost",port=3306,user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name IS '{}' ORDER BY id;".format(sys.argv[4]))
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
