#!/usr/bin/python3
"""Selects states from db"""
import sys
import MySQLdb

if __name__ == "__main__":
    """Connector for mysqldb"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]