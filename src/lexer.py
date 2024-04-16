import re

conditionals = ["si", "sino", "contrario"]
logicOperators = ["interruptor", "puerta", "cierre"]

class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code
    
    def tokenize(self):
        # Aquí vamos a guardar los tokens creados por el lexer
        tokens = {}

        # Creamos una lista de palabras del codigo fuente
        source_code = self.source_code.split()

        # Esto seguira la pista del indice de la palabra en el "source_code"
        source_index = 0

        # Iteramos a traves de cada palabra en el "source_code" para generar los tokens
        while source_index < len(source_code):

            word = source_code[source_index]

            # Esto va a reconocer una variable y crear un token para ella
            if word == "bloque": 
                self.add_to_dict(tokens, "DeclaracionEntero", word)
            
            elif word == "hiloRedstone":
                self.add_to_dict(tokens, "DeclaracionString", word)
            
            elif word == "pasoHelado":
                self.add_to_dict(tokens, "DeclaracionFloat", word)
                
            elif word == "booleanman":
                self.add_to_dict(tokens, "DeclaracionBoolean", word)
            
            elif word in conditionals:
                self.add_to_dict(tokens, "Condicional", word)
            
            elif word in logicOperators:
                self.add_to_dict(tokens, "OperadorLogico", word)
            
            elif word == "minarPara":
                self.add_to_dict(tokens, "CicloFor", word)
            
            elif word == "mientrasNoDiamante":
                self.add_to_dict(tokens, "CicloWhile", word)
            
            elif word == "picoRoto":
                self.add_to_dict(tokens, "palabraReservadaPicoRoto", word)
            
            elif word == "seguirPicando":
                self.add_to_dict(tokens, "palabraReservadaPicoRotoSeguitPicando", word)
    
            # Reconocera una palabra y creara un indentificador para esta misma
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                if word[len(word)-1] == ";":
                    self.add_to_dict(tokens, "Identificador", word[0:len(word)-1])
                else:
                    self.add_to_dict(tokens, "Identificador", word)  # aclarar
            
            # Reconocera un entero y creara un indentificador para este mismo
            elif re.match('[0-9]', word):
                if word[len(word)-1] == ";":
                    self.add_to_dict(tokens, "Entero", word[0:len(word)-1])
                else:
                    self.add_to_dict(tokens, "Entero", word)  # aclarar
            
            # Reconocera un operador y creara un indentificador para este mismo
            elif word in "=/*=-+":
                self.add_to_dict(tokens, "Operador", word)
            
            # Si un ; se encuentra al final de una palabra se agrega un token FinSentencia
            if word[len(word)-1] == ";":
                self.add_to_dict(tokens, "FinSentencia", ";")

            source_index += 1

        print(tokens)

        return tokens

    def add_to_dict(self, dictionary, key, value):
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]