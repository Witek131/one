import sqlite3
con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films 
    WHERE title LIKE 'X%'""", ()).fetchall()

used = []
for elem in result:
    if elem[0] not in used:
        print(elem[0])
        used.append(elem[0])

con.close()