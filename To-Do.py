#To-Do List: Crear un archivo de de texto. lograr modificar el achivo de texto. Features: agregar líneas, borrar lineas. Features: poder mostrar la lista y enumerar las líneas, poder agregar quehaceres en cualquier linea, borrar quehaceres, todo dentro de un menú interactivo
def decidir(pregunta, decisiones, numeros_decisiones):
    while True:
        decision = input(f'''
{pregunta}
    {decisiones}
Elija una opcion eligiendo un numero.
>>> ''').strip()
        if decision in numeros_decisiones:
            return decision
        else:
            print ("""
Elija un numero dentro de las opciones""")

def decidir_numero(pregunta, maximo):
    while True:
        try:
            numero = int (input (pregunta))
            if 0 < numero-1 <= maximo:
                return numero-1
            else:
                print ("Inserte un valor valido")
        except ValueError:
            print ("Inserte un valor valido")

def enumerar_lista(lista):
    for linea, texto in enumerate (lista):
        print (str(linea+1) + " : " + texto)

def to_do_archivo():
    nombre = input ("""Que nombre tiene su archivo?
>>> """)
    if not nombre.endswith(".txt"):
        nombre += ".txt"
    try:
        prueba_existencia = open (nombre, "r")
        prueba_existencia.close()
    except FileNotFoundError:
        decision_creacion = decidir ("La lista nombrada no existe actualmente! Desea crearla?", """1 Si
    2 No""", ("1" , "2"))
        if decision_creacion == "2":
            return " "
        elif decision_creacion == "1":
            archivo_creacion = open (nombre, "w")
            archivo_creacion.close()
    try:
        archivo = open (nombre, "a+")
        archivo.seek(0)
        lista_tareas = archivo.readlines()
        len_lista_tareas = len (lista_tareas)
        
        if not lista_tareas:
            decision_agregar = decidir ("Lo unico que tiene esta lista de tareas es polvo! Deseas agregar la primera tarea?", """1 Si
    2 No""", ("1" , "2"))
            if decision_agregar == "2":
                   return " "
            elif decision_agregar == "1":
                tarea_agregar = input ("""Escriba aqui la tarea que quiere agregar (No hace falta enumerar)
>>> """)
                archivo.write(tarea_agregar + "\n")
                print ("Agregado exitosamente!")
                return " "
            archivo.close()
    except Exception as e:
        print(f"Ha ocurrido el error '{e}'")
    while True:
        try:
            archivo = open (nombre, "r+")
            archivo.seek(0)
            lista_tareas = archivo.readlines()
            len_lista_tareas = len (lista_tareas)
            enumerar_lista(lista_tareas)
            decision_principal = decidir ("Que desea hacer con su archivo?", """1 Agregar Tarea
    2 Eliminar tarea
    3 Sobreescribir todo lo exstente con una nueva tarea
    4 Salir""", ("1", "2", "3", "4"))
            
            if decision_principal == "4":
                print ("Cumple tus deberes!")
                break
            
            elif decision_principal == "1":
                archivo.seek(0, 2)
                tarea_agregar = input ("""Escriba que otra tarea quiere agregar (No hace falta enumerar)
>>> """)
                archivo.write(tarea_agregar + "\n")
                print ("Tarea agregada con exito")
                continue
            
            elif decision_principal == "2":
                linea_eliminar = decidir_numero("Elige que tarea (linea) desea eliminar: ", len_lista_tareas)
                archivo_suplantar = open (nombre, "w")
                del lista_tareas[linea_eliminar]
                archivo_suplantar.writelines(lista_tareas)
                archivo_suplantar.close()
                print (f"Tarea '{lista_tareas[linea_eliminar]}' eliminada con exito")
                archivo.close()
                continue
                
            elif decision_principal == "3":
                sobreescritura = input ("""Escriba lo que sera su nueva primera tarea (No hace falta enumerar)
>>> """)
                archivo_sobreescribir = open (nombre, "w")
                archivo_sobreescribir.write(sobreescritura + "\n")
                print ("Tareas sobreescritas con exito")
                archivo.close()
                continue  
        except Exception as e:
            print(f"Ha ocurrido el error '{e}'")
            continue
    return "Programa finalizado."
print(to_do_archivo())