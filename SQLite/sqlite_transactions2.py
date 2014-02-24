## TRANSACTIONS
# Friends table gets created if does not exists or deleted if it does
# No commit is called to write the data to the Friends table
# However, a CREATE TABLE query is performed
# This implicitly writes the previous queries data to the Friends table

import sqlite3 as lite
import sys

try:
  con = lite.connect('test.db')
  cur = con.cursor()
  cur.execute("DROP TABLE IF EXISTS Friends")
  cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT)")
  cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
  cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
  cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
  cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")

  cur.execute("CREATE TABLE IF NOT EXISTS Temporary(Id INT)")

except lite.Error, e:
  if con:
    con.rollback()

  print "Error %s:" % e.args[0]
  sys.exit(1)

finally:
  if con:
    con.close()