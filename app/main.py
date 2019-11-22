# Code to start the app and show the menu
from .menu import creaMenu


def main():
    menu, funciones = creaMenu()

    while True:
        opcion = muestraMenu(menu)
        if not opcion.isnumeric() or len(menu)<int(opcion):
            exit()
        elif int(opcion)>0:
            funciones[menu[int(opcion)-1]]()


def muestraMenu(menu):
    for opcion in menu:
        print(opcion)
    return input("Selecciona una opcion: ")


if __name__== "__main__" :
    main()