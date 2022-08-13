import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

query = """
DROP TABLE IF EXISTS users_normalized;
DROP TABLE IF EXISTS cities_normalized;
-- Первый шаг – создание таблицы-справочника для городов
CREATE TABLE cities_normalized (
 pk INTEGER PRIMARY KEY AUTOINCREMENT,
 name VARCHAR(255)
);
-- Второй шаг – наполнение таблицы-справочника уникальными значениями;
INSERT INTO `cities_normalized` (name)
SELECT DISTINCT city FROM users_original;
-- Третий шаг – создание новой таблицы с внешним ключом;
CREATE TABLE users_normalized (
 pk INTEGER PRIMARY KEY AUTOINCREMENT,
 name VARCHAR(255),
 city_pk INTEGER,
 FOREIGN KEY (city_pk) REFERENCES cities_normalized(pk)
);
-- Четвертый шаг – наполнение нормализованной таблицы
INSERT INTO users_normalized (pk, name, city_pk)
SELECT users_original.pk, users_original.name, cities_normalized.pk
FROM users_original 
LEFT JOIN cities_normalized on cities_normalized.name = users_original.city;

"""

cur.executescript(query)

# Последний шаг - проверяем, что все получилось

con.close()
