import sqlite3

db_path = "bookdb.db"

con = sqlite3.connect(db_path)
con.row_factory = sqlite3.Row
cur = con.cursor()

try:
    cur.execute('select * from BOOKLIST where TITLE like ? and PRICE < ?', ('%Java%', 3000,))
    rows = cur.fetchall()
    if not rows:
        print("not found..")
    else:
        for row in rows:
            print("ID = %s" % str(row['ID']))
            print("TITLE = %s" % str(row['TITLE']))
            print("AUTHOR = %s" % str(row['AUTHOR']))
            print("PUBLISHER = %s" % str(row['PUBLISHER']))
            print("PRICE = %s" % str(row['PRICE']))
            print("ISBN = %s" % str(row['ISBN']))
            print("------------------------------------------") 
            

except sqlite3.Error as e:
    print("Error occurred:", e.args[0])

con.commit()
con.close()