#! /usr/bin/env python3

import sys
import io
import datetime
import cgi
import sqlite3

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
param_str = form.getvalue('param1','')

db_path = "bookdb2.db"

con = sqlite3.connect(db_path)
con.row_factory = sqlite3.Row
cur = con.cursor()


print("Content-type: text/html\n")
print("<html>")
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
print("  <body>")
try:
    cur.execute('select * from BOOKLIST where TITLE like ? or AUTHOR like ?', ('%'+ param_str +'%', '%'+ param_str +'%',))
    rows = cur.fetchall()
    if not rows:
        print("sorry.. not found..")
    else:
        print("<table border = '1'>")
        print("<tr>")
        print("<th>")
        print("ID")
        print("</th>")
        print("<th>")
        print("TITLE")
        print("</th>")
        print("<th>")
        print("AUTHOR")
        print("</th>")
        print("<th>")
        print("PUBLISHER")
        print("</th>")
        print("<th>")
        print("PRICE")
        print("</th>")
        print("<th>")
        print("ISBN")
        print("</th>")
        print("</tr>")

        for row in rows:
            print("<tr>")
            print("<td>")
            print("%d" % row['ID'])
            print("</td>")
            print("<td>")
            print("%s" % str(row['TITLE']))
            print("</td>")
            print("<td>")
            print("%s" % str(row['AUTHOR']))
            print("</td>")
            print("<td>")
            print("%s" % str(row['PUBLISHER']))
            print("</td>")
            print("<td>")
            print("%s" % str(row['PRICE']))
            print("</td>")
            print("<td>")
            print("%s" % str(row['ISBN']))
            print("</td>")
            print("</tr>")

        print("</table>")


except sqlite3.Error as e:
    print("Error occurred:", e.args[0])

print("  </body>")
print("</html>")

con.commit()
con.close()