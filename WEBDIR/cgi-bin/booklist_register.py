#! /usr/bin/env python3

#! /usr/bin/env python3

import sys
import io
import os
import cgi
import sqlite3


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
username_str = form.getvalue('username','NoValue')
password_str = form.getvalue('password','NoValue')

print("Content-type: text/html\n")
print("<html>")
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"></head>")


db_path = "userlist.db"

try:
    if os.path.isfile(db_path):
        con = sqlite3.connect(db_path)
        con.row_factory = sqlite3.Row
        cur = con.cursor()

    else:
        con = sqlite3.connect(db_path)
        con.row_factory = sqlite3.Row
        cur = con.cursor()

        cur.execute('create table USERLIST(ID int, USERNAME varchar(20) primary key, PASSWORD varchar(16))')
        line = ( 0, "admin", "0000")
        cur.execute('insert into USERLIST values (?,?,?);', line)

    try:
        
        cur.execute('select max(ID) from USERLIST')

        _id = cur.fetchone()

        line = ( _id[0]+1, username_str, password_str)

        cur.execute('insert into USERLIST values (?,?,?);', line)

        print("<body onload=\"setTimeout(location.href='/login.html',5000);\">")
        print("<p> Register is successful! </p>")
        print("<p> This page will forwaed automatically in 5 seconds, </p>")
        print("<p> if don't forward, <a href='/login.html'> click here <a> </p>")

        print("</html>")
    
        con.commit()
        con.close()

    except sqlite3.Error as e:
        print("Error occurred:", e.args[0])

        print("<body onload=\"setTimeout(location.href='/register.html?Error-Code=True',0);\"/>")
        print("</html>")

        con.commit()
        con.close()

except :
    print("<body>")
    print("Error")
    print("</body>")
    print("</html>")