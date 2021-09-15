#! /usr/bin/env python3

import sys
import io
import datetime
import cgi
import sqlite3
import requests
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
param_str = form.getvalue('param1','')
page = form.getvalue('page','0')
maxResults = form.getvalue('maxResults','40')

db_path = "bookdb.db"

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
        print("<br/>")

        url = 'https://www.googleapis.com/books/v1/volumes?q='
        response = requests.get(url+param_str+'&maxResults='+maxResults+'&startIndex='+page)
        file_path = 'url.json'

        try:
            with open(file_path, 'w') as f:
                json.dump(response.json(), f)

            with open(file_path, 'r') as f:
                data = json.load(f)

            print("<table>")
            print("<tr>")
            print("<td>")
            print("maybe...")
            print("</td>")
            print("</tr>")
            print("<tr>")

            i = 0
            offset = int(maxResults) * int(page)

            
            while True:
                try:
                    try:
                        _id = data['items'][i+offset]['id']

                        print("<td>")
                        print("<form name=\"form" + str(i) +"\" action=\"/cgi-bin/booklist_detail.py\" method=\"POST\">")
                        print("<input type=\"hidden\" name=\"id\" value=\"" + _id + "\"/>")
                        print("<input type=\"hidden\" name=\"flag\" value='1'/>")
                        print("<a href=\"javascript:form" + str(i) + ".submit()\">")

                        try:
                            imagelinks = data['items'][i+offset]['volumeInfo']['imageLinks']['thumbnail']

                        except:
                            imagelinks = '/noimage.jpg'

                        title = data['items'][i+offset]['volumeInfo']['title']

                        print("<img src=\""+ imagelinks + "\" width=\"130\" height=\"180\"/>")
                        print("<br>")
                        print(title)
                        print("</a>")
                        print("</form>")
                        print("</td>")

                        i += 1

                    except:
                        print("")
                        i += 1

                    if i == int(maxResults):
                        break

                    if i % 5 == 0:
                        print("</tr>")
                        print("<tr>")
      
                except:
                    break

            print("</tr>")
            print("</table>")

        except:
            print("")


            

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
        print("ISBN")
        print("</th>")
        print("</tr>")

        for row in rows:
            print("<tr>")
            print("<td>")
            print("%d" % row['ID'])
            print("</td>")
            print("<td>")
            print("<form name=\"form" + str(row['ID']) +"\" action=\"/cgi-bin/booklist_detail.py\" method=\"POST\">")
            print("<input type=\"hidden\" name=\"isbn\" value=\"" + str(row['ISBN']) + "\"/>")
            print("<a href=\"javascript:form" + str(row['ID']) + ".submit()\">")
            print("%s" % str(row['TITLE']))
            print("</a>")
            print("</form>")
            print("</td>")
            print("<td>")
            print("%s" % str(row['AUTHOR']))
            print("</td>")
            print("<td>")
            print("%s" % str(row['PUBLISHER']))
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