import sqlite3

with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()

    query = """
-- удаление таблиц для повторной перезаписи
    DROP TABLE IF EXISTS age_upon_outcome;
    DROP TABLE IF EXISTS animal_id;
    DROP TABLE IF EXISTS animal_type;
    DROP TABLE IF EXISTS `name`;
    DROP TABLE IF EXISTS breed;
    DROP TABLE IF EXISTS color1;
    DROP TABLE IF EXISTS color2;
    DROP TABLE IF EXISTS date_of_birth;
    DROP TABLE IF EXISTS outcome_subtype;
    DROP TABLE IF EXISTS outcome_type;
    DROP TABLE IF EXISTS outcome_month;
    DROP TABLE IF EXISTS outcome_year;
    DROP TABLE IF EXISTS cats;
        
-- создание таблицы возраста животного на момент прибытия
    CREATE TABLE age_upon_outcome (
        id INTEGER PRIMARY KEY autoincrement,
        age_id  VARCHAR(100)
    );
-- создание таблицы идентификатора животного
    CREATE TABLE animal_id (
        id INTEGER PRIMARY KEY autoincrement,
        animal_id VARCHAR(100)
    );
-- создание таблицы типа животного
    CREATE TABLE animal_type (
        id INTEGER PRIMARY KEY autoincrement,
        type_id VARCHAR(100)
    );
-- создание таблицы клички животного
    CREATE TABLE `name` (
        id INTEGER PRIMARY KEY autoincrement,
        name_id VARCHAR(100)
    );
-- создание таблицы породы животного
    CREATE TABLE breed (
        id INTEGER PRIMARY KEY autoincrement,
        breed_id VARCHAR(100)
    );
-- создание таблицы цвета животного
    CREATE TABLE color1 (
        id INTEGER PRIMARY KEY autoincrement,
        color1_id VARCHAR(100)
    );
-- создание таблицы сочетания цветов животного
    CREATE TABLE color2 (
        id INTEGER PRIMARY KEY autoincrement,
        color2_id VARCHAR(100)
    );
-- создание таблицы даты рождения животного
    CREATE TABLE date_of_birth (
        id INTEGER PRIMARY KEY autoincrement,
        date_id DATE
    );
-- создание таблицы программ для бездомных животных     
    CREATE TABLE outcome_subtype (
        id INTEGER PRIMARY KEY autoincrement,
        subtype_id VARCHAR(100)
    );
-- создание таблицы о состоянии животного 
    CREATE TABLE outcome_type (
        id INTEGER PRIMARY KEY autoincrement,
        type_id VARCHAR(100)
    );
-- создание таблицы месяц прибытия животного 
    CREATE TABLE outcome_month (
        id INTEGER PRIMARY KEY autoincrement,
        month_id INTEGER
    );
-- создание таблицы год прибытия животного
    CREATE TABLE outcome_year (
        id INTEGER PRIMARY KEY autoincrement,
        year_id INTEGER
    );
     
    
-- наполнение таблицы age_upon_outcome уникальными значениями    
    INSERT INTO age_upon_outcome (age_id)
    SELECT DISTINCT animals.age_upon_outcome FROM animals;
-- наполнение таблицы animal_id уникальными значениями    
    INSERT INTO animal_id (animal_id)
    SELECT DISTINCT animals.animal_id FROM animals;
-- наполнение таблицы animal_type уникальными значениями    
    INSERT INTO animal_type (type_id)
    SELECT DISTINCT animals.animal_type FROM animals;
-- наполнение таблицы name уникальными значениями    
    INSERT INTO `name` (name_id)
    SELECT DISTINCT animals.name FROM animals;    
-- наполнение таблицы breed уникальными значениями    
    INSERT INTO breed (breed_id)
    SELECT DISTINCT animals.breed FROM animals;    
-- наполнение таблицы color1 уникальными значениями    
    INSERT INTO color1 (color1_id)
    SELECT DISTINCT animals.color1 FROM animals;
-- наполнение таблицы color2 уникальными значениями    
    INSERT INTO color2 (color2_id)
    SELECT DISTINCT animals.color2 FROM animals;    
-- наполнение таблицы date_of_birth уникальными значениями    
    INSERT INTO date_of_birth (date_id)
    SELECT DISTINCT animals.date_of_birth FROM animals;
-- наполнение таблицы outcome_subtype уникальными значениями    
    INSERT INTO outcome_subtype (subtype_id)
    SELECT DISTINCT animals.outcome_subtype FROM animals;
-- наполнение таблицы outcome_type уникальными значениями    
    INSERT INTO outcome_type (type_id)
    SELECT DISTINCT animals.outcome_type FROM animals;
-- наполнение таблицы outcome_month уникальными значениями    
    INSERT INTO outcome_month (month_id)
    SELECT DISTINCT animals.outcome_month FROM animals;
-- наполнение таблицы outcome_year уникальными значениями    
    INSERT INTO outcome_year (year_id)
    SELECT DISTINCT animals.outcome_year FROM animals;
  
    
-- создание таблицы приведенная к нормальной форме с внешними ключами
    CREATE TABLE cats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        age_upon_outcome_id INTEGER,
        animal_id INTEGER,
        animal_type_id INTEGER,
        name_id INTEGER,
        breed_id INTEGER,
        color1_id INTEGER,
        color2_id INTEGER,
        date_of_birth_id INTEGER,
        outcome_subtype_id INTEGER,
        outcome_type_id INTEGER,
        outcome_month_id INTEGER,
        outcome_year_id INTEGER,
-- внешние ключи
        FOREIGN KEY(age_upon_outcome_id) REFERENCES age_upon_outcome(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(animal_id) REFERENCES animal_id(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(animal_type_id) REFERENCES animal_type(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(name_id) REFERENCES `name`(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(breed_id) REFERENCES breed(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(color1_id) REFERENCES color1(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(color2_id) REFERENCES color2(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(date_of_birth_id) REFERENCES date_of_birth(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(outcome_subtype_id) REFERENCES outcome_subtype(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(outcome_type_id) REFERENCES outcome_type(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(outcome_month_id) REFERENCES outcome_type(id) ON DELETE SET DEFAULT ON UPDATE CASCADE,
        FOREIGN KEY(outcome_year_id) REFERENCES outcome_type(id) ON DELETE SET DEFAULT ON UPDATE CASCADE
    );
    
-- запрос в таблицу cats по следующим столбцам
    INSERT INTO cats (
         id,
         age_upon_outcome_id,
         animal_id,
         animal_type_id,
         name_id,
         breed_id,
         color1_id,
         color2_id,
         date_of_birth_id,
         outcome_subtype_id,
         outcome_type_id,
         outcome_month_id,
         outcome_year_id
         )
-- ссыслки из таблиц 
    SELECT animals.`index`,
        age_upon_outcome.id,
        animal_id.id,
        animal_type.id,
        `name`.id,
        breed.id,
        color1.id,
        color2.id,
        date_of_birth.id,
        outcome_subtype.id,
        outcome_type.id,
        outcome_month.id,
        outcome_year.id

-- вывод информации таблицы нормальной формы с ссылками на вспомогательные таблицы       
    FROM animals 
        LEFT JOIN age_upon_outcome on age_upon_outcome.age_id = animals.age_upon_outcome
        LEFT JOIN animal_id on animal_id.animal_id = animals.animal_id
        LEFT JOIN animal_type on animal_type.type_id = animals.animal_type
        LEFT JOIN `name` on `name`.name_id = animals.name
        LEFT JOIN breed on breed.breed_id = animals.breed
        LEFT JOIN color1 on color1.color1_id = animals.color1
        LEFT JOIN color2 on color2.color2_id = animals.color2
        LEFT JOIN date_of_birth on date_of_birth.date_id = animals.date_of_birth
        LEFT JOIN outcome_subtype on outcome_subtype.subtype_id = animals.outcome_subtype
        LEFT JOIN outcome_type on outcome_type.type_id = animals.outcome_type
        LEFT JOIN outcome_month on outcome_month.month_id = animals.outcome_month
        LEFT JOIN outcome_year on outcome_year.year_id = animals.outcome_year;
          """

    index_query = """
    CREATE INDEX animals_idx ON cats (animal_id)  -- индекс для упрощения поиска (по идентификационному номеру)
    """

    cursor.executescript(query)
    cursor.executescript(index_query)
