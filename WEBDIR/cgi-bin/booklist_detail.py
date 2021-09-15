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
isbn = form.getvalue('isbn','')
id_str = form.getvalue('id','')
flag = form.getvalue('flag','')

url = 'https://www.googleapis.com/books/v1/volumes?q='

if isbn == '':
    response = requests.get(url+id_str)

else :
    response = requests.get(url+'isbn:'+isbn)

file_path = 'url.json'

print("Content-type: text/html\n")
print("<html>")
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
print("  <body>")
try:
    with open(file_path, 'w') as f:
        json.dump(response.json(), f)

    with open(file_path, 'r') as f:
        data = json.load(f)

        try:    
            title = data['items'][0]['volumeInfo']['title']
            authors = data['items'][0]['volumeInfo']['authors']
            
            try:
                _type = data['items'][0]['volumeInfo']['industryIdentifiers'][0]['type']

                if _type == 'ISBN_10':
                    isbn_10 = data['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier']
                    isbn_13 = data['items'][0]['volumeInfo']['industryIdentifiers'][1]['identifier']

                else:
                    isbn_10 = data['items'][0]['volumeInfo']['industryIdentifiers'][1]['identifier']
                    isbn_13 = data['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier']

            except:
                isbn_10 = 'Unknown'
                isbn_13 = 'Unknown'

            try:
                imagelinks = data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
            
            except:
                imagelinks = '/noimage.jpg'
            

            print("<table>")
            print("<tr>")
            print("<td rowspan = \"6\">")
            print("<img src=\""+ imagelinks + "\" width=\"130\" height=\"180\"/>")
            print("</td>")
            print("<td>")
            print("TITLE")
            print("</td>")
            print("<tr>")
            print("<td>")
            print(title)
            print("</td>")
            print("</tr>")

            print("<tr>")
            print("<td>")
            print("AUTHORS")
            print("</td>")
            print("</tr>")

            print("<tr>")
            print("<td>")
            _author = ''
            for author in authors:
                _author += author
                _author += ' '
                print(author)
            print("</td>")
            print("</tr>")

            print("<tr>")
            print("<td>")
            print("PUBLISHEDDATE")
            print("</td>")
            print("</tr>")

            try:
                publishedDate = data['items'][0]['volumeInfo']['publishedDate']
            
            except:
                publishedDate = 'Unknown'
            
            print("<tr>")
            print("<td>")
            print(publishedDate)
            print("</td>")
            print("</tr>")
            
            try:
                description = data['items'][0]['volumeInfo']['description']
                print("<tr>")
                print("<td>")
                print("DESCRIPTION")
                print("</td>")
                print("<td>")
                print(description)
                print("</td>")
                print("</tr>")

            except:
                print("")

            try:
                publisher = data['items'][0]['volumeInfo']['publisher']

            except:
                publisher = 'Unknown'
            
            print("<tr>")
            print("<td>")
            print("PUBLISHER")
            print("</td>")
            print("<td>")
            print(publisher)
            print("</td>")
            print("</tr>")

            print("<tr>")
            print("<td>")
            print("ISBN-10")
            print("</td>")
            print("<td>")
            print(isbn_10)
            print("</td>")
            print("</tr>")

            print("<tr>")
            print("<td>")
            print("ISBN-13")
            print("</td>")
            print("<td>")
            print(isbn_13)
            print("</td>")
            print("</tr>")            

            print("<tr>")
            print("<td>")
            print("BUY LINK")
            print("</td>")
            print("</tr>")

            if isbn_10 == 'Unknown':
                print("<tr>")
                print("<td>")
                print("<a href=\"https://www.amazon.co.jp/s?k=" + title + "&i=stripbooks&__mk_ja_JP=カタカナ&ref=nb_sb_noss\">")
                print("→Amazon")
                print("</a>")
                print("</td>")
                print("</tr>")
            
                print("<tr>")
                print("<td>")
                print("<a href=\"https://books.rakuten.co.jp/search?sitem="+ title + "&g=001&l-id=pc-search-box&x=0&y=0\">")
                print("→Rakuten books <br>")
                print("</a>")
                print("</td>")
                print("</tr>")
            
            else:

                print("<tr>")
                print("<td>")
                print("<a href=\"https://www.amazon.co.jp/dp/" + isbn_10 + "\">")
                print("→Amazon")
                print("</a>")
                print("</td>")
                print("</tr>")
            
                print("<tr>")
                print("<td>")
                print("<a href=\"https://books.rakuten.co.jp/search?sitem="+ isbn_10 + "&g=001&l-id=pc-search-box&x=0&y=0\">")
                print("→Rakuten books <br>")
                print("</a>")
                print("</td>")
                print("</tr>")

            if flag == '1':
                print("<tr>")
                print("<td>")
                print("<form name=\"form\" action=\"/cgi-bin/booklist_update.py\" method=\"POST\">")
                print("<input type=\"hidden\" name=\"title\" value=\""+title+"\"/>")
                print("<input type=\"hidden\" name=\"authors\" value=\""+_author+"\"/>")
                print("<input type=\"hidden\" name=\"publisher\" value=\""+publisher+"\"/>")
                print("<input type=\"hidden\" name=\"isbn\" value=\""+isbn_10+"\"/>")
                print("<button type=\"submit\" name=\"submit\">")
                print("register this book")
                print("</button>")
                print("</form>")
                print("</td>")
                print("</tr>")

            print("</table>")

        except:
            print("not found")

except:
    print("Error")


print("  </body>")
print("</html>")