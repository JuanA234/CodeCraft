import lexer

def main():

    #lee el contendio de test.lang y lo guarda en una variable
    content = ""
    with open('src/test.lang', 'r') as file:
        content = file.read()

    #lexer

    #Llamamos la clase lexer y lo inicializamos con el codigo fuente
    lex = lexer.lexer(content)
    #Ahora  llamamos al metodo "tokenize"
    tokens = lex.tokenize()


main()