import csv
import os

# Lista global en memoria requerida para almacenar las tareas
tasks_list = []
ARCHIVO_CSV = "todos.csv"

def add_one_task(title):
    """Agrega correctamente nuevas tareas a la lista activa en memoria."""
    title = title.strip()
    if title:
        tasks_list.append(title)
        print(f"✅ Tarea agregada: '{title}'")
    else:
        print("⚠️ El título de la tarea no puede estar vacío.")

def print_list():
    """Muestra las tareas en orden con posiciones legibles (base 1)."""
    print("\n--- TAREAS PENDIENTES ---")
    if not tasks_list:
        print("[La lista está vacía]")
        return
    for posicion, titulo in enumerate(tasks_list, 1):
        print(f"{posicion}. {titulo}")

def delete_task(number_to_delete):
    """Elimina la tarea correcta usando su posición numérica."""
    try:
        posicion = int(number_to_delete)
        if 1 <= posicion <= len(tasks_list):
            tarea_eliminada = tasks_list.pop(posicion - 1)
            print(f"🗑️ Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("⚠️ Número fuera de rango. Revisa la lista.")
    except ValueError:
        print("⚠️ Por favor, introduce un número entero válido.")

def save_todos():
    """Guarda las tareas actuales de la memoria en todos.csv."""
    try:
        with open(ARCHIVO_CSV, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo)
            for tarea in tasks_list:
                escritor.writerow([tarea])
        print(f"💾 Tareas guardadas exitosamente en '{ARCHIVO_CSV}'.")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")

def load_todos():
    """Reconstruye correctamente las tareas desde todos.csv como strings puros."""
    global tasks_list
    if not os.path.exists(ARCHIVO_CSV):
        tasks_list = []
        return
    
    tasks_list = []
    try:
        with open(ARCHIVO_CSV, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if fila:  # ¡CORREGIDO! Extrae el string puro del primer elemento
                    tasks_list.append(fila[0])
        print(f"📂 Tareas cargadas desde '{ARCHIVO_CSV}'.")
    except Exception as e:
        print(f"❌ Error al cargar el archivo: {e}")

def menu_cli():
    """Flujo interactivo de la línea de comandos."""
    # Cargar las tareas existentes al iniciar el programa
    load_todos()
    
    while True:
        print("\n=========================")
        print("   GESTOR DE LOGÍSTICA   ")
        print("=========================")
        print("1. Mostrar tareas")
        print("2. Agregar tarea por título")
        print("3. Eliminar tarea por posición")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            print_list()
        elif opcion == "2":
            titulo = input("Introduce el título de la nueva tarea: ")
            add_one_task(titulo)
        elif opcion == "3":
            print_list()
            if tasks_list:
                numero = input("Introduce el número de la tarea a eliminar: ")
                delete_task(numero)
        elif opcion == "4":
            save_todos()
            print("\n¡Cierre de turno completado! Datos guardados localmente.")
            break
        else:
            print("⚠️ Opción no válida. Elige un número del 1 al 4.")

if __name__ == "__main__":
    menu_cli()
