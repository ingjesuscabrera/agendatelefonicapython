# Inicializar una agenda vacía
agenda_telefonica = {}

# Función para agregar un contacto
def agregar_contacto(nombre, telefono):
    agenda_telefonica[nombre] = telefono
    print(f'Contacto {nombre} agregado con éxito.')

# Función para buscar un contacto
def buscar_contacto(nombre):
    if nombre in agenda_telefonica:
        print(f'Nombre: {nombre}, Teléfono: {agenda_telefonica[nombre]}')
    else:
        print(f'El contacto {nombre} no se encuentra en la agenda.')

# Función para mostrar todos los contactos
def mostrar_contactos():
    if agenda_telefonica:
        print("Lista de Contactos:")
        for nombre, telefono in agenda_telefonica.items():
            print(f'Nombre: {nombre}, Teléfono: {telefono}')
    else:
        print("La agenda telefónica está vacía.")

# Función para eliminar un contacto
def eliminar_contacto(nombre):
    if nombre in agenda_telefonica:
        del agenda_telefonica[nombre]
        print(f'Contacto {nombre} eliminado con éxito.')
    else:
        print(f'El contacto {nombre} no se encuentra en la agenda.')

# Loop principal para interactuar con la agenda
while True:
    print("\nAgenda Telefónica")
    print("1. Agregar Contacto")
    print("2. Buscar Contacto")
    print("3. Mostrar Contactos")
    print("4. Eliminar Contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        agregar_contacto(nombre, telefono)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        buscar_contacto(nombre)
    elif opcion == "3":
        mostrar_contactos()
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        eliminar_contacto(nombre)
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
