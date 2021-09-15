#! /usr/bin/env python3

import sys
import io
import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
dt_now = datetime.datetime.now()

print("Content-type: text/html\n")
print("<html>")
print("  <head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/></head>")
print("  <body>システムアーキテクトプログラミング演習</body>")
print(dt_now)
print("</html>")