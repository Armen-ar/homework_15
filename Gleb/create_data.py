import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

# Сперва создаем исходную таблицу

query = """ 
DROP TABLE IF EXISTS users_original;
CREATE TABLE users_original (
 `pk` INTEGER PRIMARY KEY AUTOINCREMENT,
 `name` VARCHAR(255),
 `city` VARCHAR(255)
);
INSERT INTO users_original (city, name) VALUES ('Саратов','Василий');
INSERT INTO users_original ('city','name') VALUES  ('Норильск','Александр');
INSERT INTO users_original ('city','name') VALUES ('Москва','Валерия');
INSERT INTO users_original ('city','name') VALUES ('Казань','Дарья');
INSERT INTO users_original ('city','name') VALUES ('Уфа','Игорь');
INSERT INTO users_original ('city','name') VALUES ('Новосибирск','Татьяна');
INSERT INTO users_original ('city','name') VALUES ('Саратов','Георгий');
INSERT INTO users_original ('city','name') VALUES ('Иркутск','Валентина');
INSERT INTO users_original ('city','name') VALUES ('Москва','Дмитрий');
INSERT INTO users_original ('city','name') VALUES ('Казань','Ринат');

"""

cur.executescript(query)

con.close()
