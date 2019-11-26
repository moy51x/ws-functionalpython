# Code to start the app and show the menu
from .menu import creaMenu
from .constants import METHOD_TOP_ARTISTS, METHOD_TOP_TRACKS

def main():
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
                ejecutaOpcion(menu, funciones, opcion)


def muestraMenu(menu):
    for opcion in menu:
        print(opcion)
    return input("Selecciona una opcion: ")


def ejecutaOpcion(menu, funciones, opcion):
    opcion_seleccionada = menu[opcion]
    funcion = funciones[opcion_seleccionada]
    if opcion_seleccionada == menu[0]:
        funcion(METHOD_TOP_ARTISTS) #Descarga Top Artistas
    elif opcion_seleccionada == menu[1]:
        funcion(METHOD_TOP_TRACKS) #Descarga Top Tracks
    else:
        funcion()
        

if __name__== "__main__" :
    main()