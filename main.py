from colorama import Fore, Back, Style
import sqlite3
import pyfiglet
import visual as vs
import os
import platform
import time
import webbrowser

option = None #en este momento mi variabel opcion es igual a nada 

#creando mi base de datos 
rutDataBase = os.path.join('data', 'data.db') #ruta de mi base de datos que esta en la carpeta data, y el archivo se data.db
conexion = sqlite3.connect(rutDataBase) #conectando mi base de datos
cursor = conexion.cursor() #creando cursor de mi base de datos con lo cual vamos a consultar y modificar mi base de datos 

cursor.execute('''
               CREATE TABLE IF NOT EXISTS ToDoList(
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   act TEXT NOT NULL
               )
               
               ''') #Creando tabla, una fila es de el id(unico y autoincremental), title(Es texto y no puede ser nulo) al igual que act

conexion.commit()#agregando todos nuestros cambios a nuestra base de datos

#funciones generales 

def clearConsole():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')    

#funcionesCall

def call(op):
    if op == 1:
        console()
    elif op == 2:
        vs.vs()
    else:
        webbrowser.open('https://github.com/LUISEDOCCOR')           

def console(): #modo consola
    option = None 
    while option != 1 and option != 2 and option != 3:
        clearConsole()
        print(Fore.RED + 'Select an option \n' + Style.RESET_ALL)
        print('Option 1 = Add')
        print('Option 2 = Remove')
        print('Option 3 = See')
        print('\n')
        option = int(input('Which option do you choose: '))
    #add
    if option == 1:
        x = int(input('Activities to add: ')) #preguntamos actividades por añadir
        for i in range(x): 
            clearConsole() #limpiamos consola
            print(f'Activity Num: {i+1}') #printamos el numero de actividad que es 
            title = input(f'Title Default: [Act] ')#preguntamos la data por agregar
            if title == '':
                title = 'Activity: '
            act = input('Activity: ') #preguntamos la data por agregar
            cursor.execute('INSERT INTO ToDoList (title, act) VALUES (?,?)', (title, act)) #insertamos en nuestra base de dattos esta infromación
        conexion.commit()
        clearConsole()
        see()#Guardamos todos lo cambios en ella 
    elif option == 2:
        option = True
        while option:
            clearConsole()
            see()
            actToDelete = input(Fore.BLUE + 'Activity to delete [ID]: ' + Style.RESET_ALL)
            cursor.execute('DELETE FROM ToDoList WHERE id = ?', (actToDelete)) 
            conexion.commit() 
            clearConsole()
            see()  
            print('\n')
            x = input('Delete more (s/n): ')
            x.lower
            if x != 's':
                option = False
                
                
    else:
        clearConsole()
        see()



def see():
    cursor.execute('SELECT * FROM ToDoList')
    acts = cursor.fetchall()  #nuestra consulta la vuelve en una lista de tuplas
    if not acts:
        print(Fore.RED + 'No activities' + Style.RESET_ALL)
    else:
        for act in acts:
            print(f'''
            {Fore.RED} Activity ID: {act[0]} {Style.RESET_ALL}
            Title: {act[1]}
            Activity: {act[2]}
            ''')



clearConsole()
print(Fore.MAGENTA + pyfiglet.figlet_format("To Do App"))
print(Fore.RED + pyfiglet.figlet_format("By Luis") + Style.RESET_ALL)
time.sleep(1)
clearConsole()

while option != 1 and option != 2 and option != 3:
    print(Fore.RED + 'Select an option \n' + Style.RESET_ALL)
    print('Option 1 = Console Mod')
    print('Option 2 = Graphical Mod')
    print('Option 3 = GitHub Code')
    print('\n')
    option = int(input('Which option do you choose: '))
    clearConsole()
    call(option)

 