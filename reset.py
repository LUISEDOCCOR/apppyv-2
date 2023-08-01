import os
import sqlite3



rutDataBase = os.path.join('data', 'data.db')
conexion = sqlite3.connect(rutDataBase)
cursor = conexion.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS ToDoList(
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   act TEXT NOT NULL
               )
               
               ''')
conexion.commit()

cursor.execute('DELETE FROM ToDoList')
conexion.commit()
conexion.close()