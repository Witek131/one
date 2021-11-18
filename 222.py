# coding: utf-8
# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect(input())
print("Hell")
# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT * FROM films WHERE title like 'Х%'""").fetchall()
print(result)
# Вывод результатов на экран
arr = []
for i in result:
    s = i[2]
    if s not in arr:
        arr.append(s)
        print(s)

con.close()
# films_db.sqlite
