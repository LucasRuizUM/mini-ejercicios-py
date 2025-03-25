#agenda en python para almacenar apellidos y numeros de telefono y que a partir del apellido me devuelva el numero de telefono correspondiente



agenda_telefonica = {}

def agregar_contacto (nombre, telefono):

    agenda_telefonica[nombre] = telefono
    print (f'Contacto {nombre} agregado con exito.')


def buscar_contacto (nombre):

    if nombre in agenda_telefonica:
        print (f'nombre: {nombre}, telefono: {agenda_telefonica[nombre]}')

    else:
        print(f'el contacto {nombre} no se encuentra en la agenda.')


def mostrar_contacto():
    if agenda_telefonica:
        print("lista de contactos;")
        for nombre, telefono in agenda_telefonica.items():
            print (f'nombre: {nombre}, telefono: {telefono}')

    else:
        print("la agenda telefonica esta vacia")


def eliminar_contacto(nombre):
    if nombre in agenda_telefonica:
        del agenda_telefonica[nombre]
        print(f'el contacto {nombre} no se encuentra en la agenda.')


while True:
    print("\nAgenda telefonica")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print ("4. Eliminar contactos")
    print ("5. Salir")

    opcion = input("seleccione una opcion:  ")

    if opcion == "1":
        nombre = input ("ingrese el nombre del contacto:  ")
        telefono = input ("ingrse el telefono del contacto:  ")
        agregar_contacto(nombre, telefono)
    elif opcion == "2":
        nombre = input ("ingrese el contacto a buscar:  ")
        buscar_contacto(nombre)

    elif opcion == "3":
        mostrar_contacto()
    elif opcion == "4":
        nombre = input("ingrese el nombre del contacto a eliminar:  ")
        eliminar_contacto(nombre)

    elif opcion == "5":
        break
    else:
        print("opcion no valida seleccione uan opcion valida")


