import mysql.connector

# Подключение к базе данных
connection = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='Друзья_человека'
)

# Создание курсора
cursor = connection.cursor()

# Пример создания таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Домашние_животные (
    id INT AUTO_INCREMENT PRIMARY KEY,
    имя VARCHAR(50),
    дата_рождения DATE
)
''')

# Пример вставки данных
cursor.execute('''
INSERT INTO Домашние_животные (имя, дата_рождения)
VALUES (%s, %s)
''', ('Барсик', '2021-05-10'))

# Фиксация изменений
connection.commit()

# Пример выборки данных
cursor.execute('SELECT * FROM Домашние_животные')
for row in cursor.fetchall():
    print(row)

# Закрытие курсора и соединения
cursor.close()
connection.close()
