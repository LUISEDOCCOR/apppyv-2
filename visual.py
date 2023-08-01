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

title = None
act = None
maxId = []


def vs():
    global title,act #Definimos nuestras variables globales, que es el titulo y la actividad para que desde cualquier funcion se puedan ejecutar
    
    def insert(): #funcion para insertar en nuestra data
        newTitle = title.get() # obtenemos el valor de nuestro 
        newAct = act.get("1.0", tk.END) # obtenemos el valor de nuestra act 
        if newTitle == '': #si el titulo esta vacio le ponemos el valor Act
            newTitle = 'Activity'
        cursor.execute('INSERT INTO ToDoList (title, act) VALUES (?,?)',(newTitle, newAct))  #insertamos valores en nuestra base de datos
        conexion.commit()  #guardamos lo cambios 
        title.delete(0, tk.END)
        act.delete("1.0", tk.END)
        title.insert(0, 'Activity: ')    
    
    #creando ventana
    root = tk.Tk()
    root.title('To Do App')
    root.geometry("400x300")
    root.focus_force()
    #contenido ventana
   
   #Agrgar actividad
    tk.Label(root, text='Activity to add: ', font=('Arial',15)).pack(pady=10)
    
    #title
    title = tk.Entry(root, font=('Arial', 15))
    title.insert(0, 'Activity: ')
    title.pack(pady=20)
    
    #act
    act = tk.Text(root, font=('Arial', 15), width=20, height=5)
    act.pack(pady=7)
    
    #recolectar datos 
    tk.Button(root, text='Add', justify='center', font=('Arial', 12), command=insert).pack(pady=5)
    root.mainloop()

