import tkinter as tk
import sqlite3
import os

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


def vs():
    root = tk.Tk()#creando ventana
    root.title('To Do App')
    root.geometry("500x300")
    mensajePrincipal = tk.Label(root, text='To Do App', font=('Arial', 20))
    mensajePrincipal.pack()
    
    root.mainloop()
vs()