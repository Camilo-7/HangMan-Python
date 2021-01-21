from os import system
from hangMan import HangMan
from game import Game
class NuevoJuego:


    if __name__ == '__main__':
        
        system("cls")

        f = open("palabras/HangMan.txt","r")
        texto = f.read()
        print(texto)
        f.close()

        print("\n \nBienvenido al juego Hangman por favor elige una de las siguiente opciones \n")
        print("cantidad de oportunidades 4, 6, 8")
        
        oportunities = 0
        checked = False
        while checked == False:
            oportunities = input("elección: ")
            if oportunities == "4" or oportunities == "6" or oportunities == "8":
                print("\nHas elegido cantidad de " + str(oportunities) + " equivocaciones permitidas\n \n")
                oportunities = int(oportunities)
                checked = True
            else:
                print("\n debe seleccionar un numero de oportunidades valido, que puede ser 4, 6 o 8 \n")

        #newGame = HangMan(True, oportunities)
        newGame = Game(True, oportunities)
