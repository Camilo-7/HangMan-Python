import random
from os import system
class HangMan:

    # Atributos
    #--------------------------------------------------------------------------------------

    onGame   = bool
    completeWord = bool
    oportunities = int
    words = []
    indexWord = []
    selectedLetters = str

    # Método Constructor
    #--------------------------------------------------------------------------------------
    # inicializa el juego con la cantidad de intentos seleccionados por el usuario
    # Se lee el archivo txt donde se encuentran las palabras del juego y se incorporan a la lista words[] 
    def __init__(self, onGame, oportunities):
        self.onGame = onGame
        self.oportunities = oportunities
        self.loadWords()
        self.orderRandom()
        self.get_beginGame()

    # Métodos
    #--------------------------------------------------------------------------------------
    # Lee el archivo de texto donde se encunetran registradas las palabras del juego y las incorpora a la lista words[]
    def loadWords(self):
        f = open("palabras/ListaPalabras.txt")
        for line in f.readlines():
            self.words.append(line.replace("\n",""))
        f.close()

    # ordena al azar la lista words[], requiere la importación de la libreria random
    def orderRandom(self):
        random.shuffle(self.words)   

    #registerIndexWords se crea una lista cuya longitud es igual a la cantidad de caracteres que tiene la palabra del vector words[] que ingresa como parámetro 
    def registerIndexWords(self, i):

        wordA = self.words[i]
        longA = len(wordA)
        for letter in wordA:
            self.indexWord.append(False)

    #def inicia el juego
    def get_beginGame(self):
        tries = 0
        self.completeWord = False
        self.selectedLetters = ""
        self.registerIndexWords(0) #aquí se debe elegir que palabra de la lista va

        while self.onGame:
            self.get_paint(tries)
            self.get_word(0) #aquí se debe elegir que palabra de la lista va
            if self.completeWord:
                self.get_paint(0)
                self.onGame = False
                break
            selectedLetter = input("\n \n" +self.words[0] + " digita una letra: ")
            self.selectedLetters = self.selectedLetters + selectedLetter + " " 
            counter = 0
            happend = False

            for letter in self.words[0]:
                if selectedLetter == letter:
                    self.indexWord[counter] = True
                    happend = True
                counter +=1

            if happend == False:
                tries +=1

            left = self.oportunities - tries
            if left == 0:
                self.get_paint(8)
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
        if self.completeWord:
            print("\n \n" + "FELICITACIONES HAS GANADO" + "\n \n")
        elif tries == 8:
            print("\n \n" + "HAS PERDIDO SIEMPRE TE RECORDAREMOS COMO EL PIBE QUE NO PUDO ADIVINAR, QUE LA FUERZA TE ACOMPAÑE" + "\n \n")

    # pinta en la consola los espacios de las letras ocultas y muestra las letras acertadas
    def get_word(self, i):
        wordA = self.words[i]
        long = 0
        palabra = ""
        for wletter in wordA:
            if self.indexWord[long] == False:
                palabra = palabra + " _"
            else:
                palabra = palabra + wletter
            long +=1
        if palabra == wordA:
            self.completeWord = True
        print(palabra)
