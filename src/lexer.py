import re

class lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code
    
    def tokenize(self):
        #Aquí vamos a guardar los tokens creados por el lexer
        tokens = []

        #Creamos una lista de palabras del codigo fuente
        source_code = self.source_code.split()

        #Esto seguira la pista del indice de la palabra en el "source_code"
        source_index = 0

        #Iteramos a traves de cada palabra en el "source_code" para generar los tokens
        while source_index < len(source_code):

            word = source_code[source_index]

            #Esto va a reconocer una variable y crear un token para ella
            if word == "bloque": 
                tokens.append(["DeclaracionEntero", word])

            #Reconocera una palabra y creara un indentificador para esta misma
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                if word[len(word)-1] == ";":
                    tokens.append(['Identificador', word[0:len(word)-1]])
                else:
                    tokens.append(['Identificador', word]) #aclarar
            
            #Reconocera un entero y creara un indentificador para este mismo
            elif re.match('[0-9]', word):
                if word[len(word)-1] == ";":
                    tokens.append(['Entero', word[0:len(word)-1]])
                else:
                    tokens.append(['Entero', word]) #aclarar
            
            ##Reconocera un operador y creara un indentificador para este mismo
            elif word in "=/*=-+":
                tokens.append(['Operador', word])
            
            #Si un ; se encuentra al final de una palabra se agrega un token FinSentencia
            if word[len(word)-1] == ";":
                tokens.append(['FinSentencia', ";"])

            source_index += 1

        print(tokens)

        #Retorna los tokens creados
        return tokens
