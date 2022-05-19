import sqlite3

connection = sqlite3.connect('shortURL.db')


with open('url.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO shortURL (URL, shortURL) VALUES (?, ?)",
            ('https://www.thepythoncode.com/article/make-url-shortener-in-python', 'https://cutt.ly/aHEU3dk')
            )

connection.commit()
connection.close()

