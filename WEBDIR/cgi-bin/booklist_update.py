import sys
import io
import csv
import cgi
import sqlite3

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
param_title = form.getvalue('title','')
param_author = form.getvalue('authors','')
param_publisher = form.getvalue('publisher','')
param_isbn = form.getvalue('isbn','')

db_path = "bookdb.db"

con = sqlite3.connect(db_path)
cur = con.cursor()

print("Content-type: text/html\n")
print("<html>")
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
print("  <body>")
try:
    if param_title == '' or param_author == '' or param_publisher == '' or param_isbn == '':
        print("please input all keys")

    else:
        cur.execute('select max(ID) from BOOKLIST')

        _id = cur.fetchone()
        line = (_id[0]+1, param_author, param_title, param_publisher, param_isbn)
    
        cur.execute('insert into BOOKLIST values (?,?,?,?,?);', line)

except sqlite3.Error as e:
	print("Error occurred:", e.args[0])

print("  </body>")
print("</html>")

con.commit()
con.close()