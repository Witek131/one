# coding: utf-8
import sqlite3


def a(n):
    con = sqlite3.connect(n)
    cur = con.cursor()

    cur.execute(
        """DELETE FROM films WHERE title like 'А%н'""")
    con.commit()
    con.close()
    # Получили результат запроса, который ввели в текстовое поле


a('films_db.sqlite')
