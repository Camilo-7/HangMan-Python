import random
from os import system
from word import Word
class Game:
    # Atributos
    #--------------------------------------------------------------------------------------

    words = []
    onGame   = bool
    oportunities = int
    selectedLetters = str
    number = int

    # Método Constructor
    #--------------------------------------------------------------------------------------
    # inicializa el juego con la cantidad de intentos seleccionados por el usuario
    # Se lee el archivo txt donde se encuentran las palabras del juego y se incorporan a la lista words[] 
    def __init__(self, onGame, oportunities):
        self.onGame = onGame
        self.oportunities = oportunities
        self.selectedLetters = ""
        self.loadWords()
        self.orderRandom()      
        self.get_beginGame()


    # Métodos
    #--------------------------------------------------------------------------------------
    # Lee el archivo de texto donde se encunetran registradas las palabras del juego y las incorpora a la lista words[]
    def loadWords(self):
        f = open("palabras/ListaPalabras.txt")
        for line in f.readlines():
            x = line.replace("\n","") #Quita el caracter de salto de linea de la palabra de lo contrario figuraría como un caracter extra en cada palabra
            x = x.strip() #quita los espacios en blanco del texto, es decir si hay un espacio final lo quita
            x = x.lower() #si en el archivo se escribió alguna letra en mayúscula, los pone en minúscula
            palabra = Word(x.strip())
            self.words.append(palabra)
        f.close()

    # ordena al azar la lista words[], requiere la importación de la libreria random
    def orderRandom(self):
        random.shuffle(self.words)   


    # def inicia el juego
    def get_beginGame(self):
        tries = 0
        self.number = 0

        while self.onGame:
            self.get_paint(tries)
            print(self.words[self.number].showWord())
            selectedLetter = input("\n \n" + " digita una letra: ")
            self.selectedLetters = self.selectedLetters + selectedLetter + " " 
            
            match = self.words[self.number].mathLetter(selectedLetter)
#            selec = input(match)
            if match == False: #Verifica que la letra registrada esté en la palabra, si no está suma un intento
                tries +=1
            
            if self.words[self.number].complete: # valida si la palabra está completa, si lo es gana el juego y finaliza
                self.get_paint(0)
                print("\n \n" + "FELICITACIONES HAS GANADO" + "\n \n")
                tries = 0
                self.continueGame()

            left = self.oportunities - tries
            if left == 0: #Verifica que todavía hayan intentos, si ya no hay, termina el juego
                self.get_paint(8)
                print("\n\nHAS PERDIDO SIEMPRE TE RECORDAREMOS COMO EL PIBE QUE NO PUDO ADIVINAR LA PALABRA: \n")
                print(self.words[self.number].word + "\n")
                print("QUE LA FUERZA TE ACOMPAÑE \n")
                tries = 0               
                self.continueGame()


    # inicia otra palabra
    def continueGame(self):
        continueGame = input("Desea cargar otra palabra digite (y) de lo contrario digite (n): ")
        if continueGame == "y":
            self.number +=1
            self.selectedLetters = ""
            system("cls")
            if self.number == len(self.words):
                print("se han completado todas las palabras del juego, gracias por jugar")
                self.onGame = False
        else:
            self.onGame = False


    #Pinta la horca, dependiendo de los intentos que lleve
    def get_paint(self, tries):
        system("cls")
        nameFile = "palabras/" + str(tries) + "HangMan.txt"
        f = open(nameFile,"r")
        texto = f.read()
        print(texto)
        f.close()
        print("\n \n" + self.selectedLetters + "\n \n")


# Método Main
#--------------------------------------------------------------------------------------

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

        newGame = Game(True, oportunities)
