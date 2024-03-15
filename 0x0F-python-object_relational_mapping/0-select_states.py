#!/usr/bin/python3
#  lists all states from the database hbtn_0e_0_usa
import MYSQLdb
import sys

if __name__ == "__main__":
	db = MYSQL.db.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
	c = db.cursor()
	c.execute("SELECT * FROM `states`")
	[print(state) for state in c.fetchall()]
