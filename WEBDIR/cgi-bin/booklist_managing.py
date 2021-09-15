#! /usr/bin/env python3

import sys
import io
import os
import cgi

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
username_str = form.getvalue('username','NoValue')

print("Content-type: text/html\n")
print("<html>\
        <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\
            <title>\
                書籍管理システム\
            </title>\
        </head>\
        <body>\
          <h3> Hello! " + username_str + "! <h3>\
          <h2>書籍検索</h2>\
          <form name=\"form1\" action=\"/cgi-bin/booklist_search.py\" method=\"POST\">\
            検索ワードを入力してください\
            <input type=\"text\" name=\"param1\"/>\
            <input type=\"hidden\" name=\"username\" value='" + username_str + "'/>\
            <button type=\"submit\" name=\"submit\">検索</button>\
          </form>\
        </body>\
        <body>\
          <h2> 書籍登録</h2>\
          <form name=\"form2\" action=\"/cgi-bin/booklist_update.py\" method=\"POST\">\
          <input type=\"hidden\" name=\"username\" value='" + username_str + "'/>\
          <table border=\"1\">\
            <tr>\
              <td>\
                TITLE\
              </td>\
              <td>\
                <input type=\"text\" name=\"title\" style=border:none;/>\
              </td>\
            </tr>\
            <tr>\
              <td>\
                AUTHOR\
              </td>\
              <td>\
                <input type=\"text\" name=\"authors\" style=border:none;/>\
              </td>\
            </tr>\
            <tr>\
              <td>\
                PUBLISHER\
              </td>\
              <td>\
                <input type=\"text\" name=\"publisher\" style=border:none;/>\
              </td>\
            </tr>\
            <tr>\
              <td>\
                ISBN\
              </td>\
              <td>\
                <input type=\"text\" name=\"isbn\" style=border:none;/>\
              </td>\
            </tr>\
          </table>\
          <button type=\"submit\" name=\"submit2\">登録</button>\
        </form>\
      </body>\
    </html>")