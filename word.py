class Word:

    # Atributos
    #--------------------------------------------------------------------------------------

    complete = bool
    word = str
    indexWord = str

    # Método Constructor
    #--------------------------------------------------------------------------------------
    def __init__(self, word):
        self.word = word
        self.complete = False
        self.indexWord = ""
        for letter in word:
            self.indexWord = self.indexWord + "_"

    # Métodos
    #--------------------------------------------------------------------------------------          
    #recibe una letra por parámetro, si reconoce esta letra dentro de la palabra en juego, pone en su indice verdadero de modo que al pintar la palabra se vean los aciertos
    def mathLetter(self, sletter):
        word = ""
        happend = False
        for position in range(len(self.word)):
            if self.word[position] == sletter:
                word = word + sletter
                happend = True
            elif self.indexWord[position] != "_":
                word = word + self.indexWord[position]
            else:
                word = word + "_"
        self.indexWord = word
        self.isComplete()
        return happend
    
    # retorna la palabra del objeto, como visible o no visible
    def showWord(self):
        word = ""
        for wletter in self.indexWord:
            if wletter == "_":
                word = word + " _"
            else:
                word = word + wletter
        return word

    # informa si la palabra ya fue descubierta o no
    def isComplete(self):
        if self.word == self.indexWord:
            self.complete = True
        else:
            self.complete = False
