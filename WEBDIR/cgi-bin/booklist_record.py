#! /usr/bin/env python3

import sys
import io
import datetime
import cgi
import sqlite3

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
param_title = form.getvalue('title','')
param_author = form.getvalue('author','')
param_price = form.getvalue('price','')
param_publisher = form.getvalue('publisher','')
param_isbn = form.getvalue('isbn','')

db_path = "bookdb.db"

con = sqlite3.connect(db_path)
con.row_factory = sqlite3.Row
cur = con.cursor()


print("Content-type: text/html\n")
print("<html>")
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
print("  <body>")

cur.execute('select ID from BOOKLIST')

try:
    for row in rows:
       a += 1; 
    cur.execute('insert into BOOKLIST value(?,?,?,?,?,?)', (row['ID']+1, param_title, param_author, param_publisher, param_price, param_isbn))
    rows = cur.fetchall()


except sqlite3.Error as e:
    print("Error occurred:", e.args[0])

print("  </body>")
print("</html>")

con.commit()
con.close()