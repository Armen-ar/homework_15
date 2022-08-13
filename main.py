import sqlite3

with sqlite3.connect("animal.db") as connection:

    cursor = connection.cursor()
    query = """
        SELECT animal_id.animal_id,
       age_upon_outcome.age_id,
       animal_type.type_id,
       `name`.name_id,
       breed.breed_id,
       color1.color1_id,
       color2.color2_id,
       date_of_birth.date_id,
       outcome_subtype.subtype_id,
       outcome_type.type_id,
       outcome_month.month_id,
       outcome_year.year_id
       
       FROM cats
    LEFT JOIN animal_id ON cats.animal_id = animal_id.id
    LEFT JOIN age_upon_outcome ON cats.age_upon_outcome_id = age_upon_outcome.id
    LEFT JOIN animal_type ON cats.animal_type_id = animal_type.id
    LEFT JOIN name ON cats.name_id = name.id
    LEFT JOIN breed ON cats.breed_id = breed.id
    LEFT JOIN color1 ON cats.color1_id = color1.id
    LEFT JOIN color2 ON cats.color2_id = color2.id
    LEFT JOIN date_of_birth ON cats.date_of_birth_id = date_of_birth.id
    LEFT JOIN outcome_subtype ON cats.outcome_subtype_id = outcome_subtype.id
    LEFT JOIN outcome_type ON cats.outcome_type_id = outcome_type.id
    LEFT JOIN outcome_month ON cats.outcome_month_id = outcome_month.id
    LEFT JOIN outcome_year ON cats.outcome_year_id = outcome_year.id
    WHERE animal_id.animal_id = 'A670420';
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(f"Идентификационный номер - {row[0]}\nВозраста животного на момент прибытия - {row[1]}\n"
              f"Тип - {row[2]}\nКличка - {row[3]}\nПорода - {row[4]}\n"
              f"Цвет - {row[5]}\nСочетания цвета - {row[6]}\nДаты рождения - {row[7]}\n"
              f"Программ для бездомных животных - {row[8]}\nСостоянии животного - {row[9]}\n"
              f"Месяц прибытия - {row[10]}\nГод прибытия - {row[11]}\n")
