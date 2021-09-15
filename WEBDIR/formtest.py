#! /usr/bin/env python3

import sys
import io
import datetime
import cgi

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()
param_str = form.getvalue('param1','')


print("Content-type: text/html\n")
print("<html>")
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
print("  <body>")
print("入力された文字は「")
print(param_str)
print("」です")
print("  </body>")
print("</html>")