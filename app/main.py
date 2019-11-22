# Code to start the app
from .menu import creaMenu

def main():
    menu = creaMenu()

    while True:
        for opcion in menu:
            print(opcion)
        opcion = input("Selecciona una opcion: ")
        if not opcion.isnumeric() or len(menu)<int(opcion):
            exit()

if __name__== "__main__" :
    main()