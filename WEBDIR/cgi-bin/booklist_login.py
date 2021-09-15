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
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>")
print("<script type=\"text/javascript\">")
print("function postForm(value, url, input_name) {\
            var form = document.createElement('form');\
            var request = document.createElement('input');\
        \
            form.method = 'POST';\
            form.action = url;\
        \
            request.type = 'hidden';\
            request.name = input_name;\
            request.value = value;\
        \
            form.appendChild(request);\
            document.body.appendChild(form);\
        \
            form.submit();\
        }")
print("</script>")
print("</head>")


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
        cur.execute('select * from USERLIST where USERNAME like ? and PASSWORD like ?', (username_str, password_str,))
        rows = cur.fetchall()

        if not rows:
            print("<body onload=\"setTimeout(location.href='/login.html?Error-Code=True',0);\"/>")
            print("</html>")
    
        else:
            print("<body onload=\"postForm('" + username_str + "', '/cgi-bin/booklist_managing.py', 'username');\"/>")
            print("</html>")

        con.commit()
        con.close()

    except sqlite3.Error as e:
        print("Error occurred:", e.args[0])

        con.commit()
        con.close()

except :
    print("<body>")
    print("Error")
    print("</body>")
    print("</html>")