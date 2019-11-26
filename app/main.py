# Code to start the app and show the menu
from .menu import creaMenu
from .constants import METHOD_TOP_ARTISTS, METHOD_TOP_TRACKS


def main():
    datos = {}
    menu, funciones = creaMenu()

    while True:
        opcion = muestraMenu(menu)
        if not opcion.isnumeric():
            exit()
        else:
            opcion = int(opcion)-1
            if opcion > len(menu):
                print("Opcion invalida!")
            elif int(opcion)>=0:
                datos = ejecutaOpcion(menu, funciones, datos, opcion)


def muestraMenu(menu):
    for opcion in menu:
        print(opcion)
    return input("Selecciona una opcion: ")


def ejecutaOpcion(menu, funciones, datos, opcion):
    opcion_seleccionada = menu[opcion]
    funcion = funciones[opcion_seleccionada]
    if opcion_seleccionada == menu[0]:
        datos = funcion(METHOD_TOP_ARTISTS) #Descarga Top Artistas
        #print(datos)
    elif opcion_seleccionada == menu[1]:
        datos = funcion(METHOD_TOP_TRACKS) #Descarga Top Tracks
        #print(datos)
    elif opcion_seleccionada == menu[4]: #Muestra los datos
        funcion(datos)
    else:
        funcion()
    
    return datos
        


if __name__== "__main__" :
    main()