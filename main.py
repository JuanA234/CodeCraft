import src.lexer as lexer
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Aplica CORS a toda la aplicación

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/lexer', methods=['POST'])
def main(): 
   
    #lee el contendio de test.lang y lo guarda en una variable
    """
    content = ""
    with open('src/test.lang', 'r') as file:
        content = file.read()
   """
    
    content = request.json['content']
    
   #lexer
    #Llamamos la clase lexer y lo inicializamos con el codigo fuente
    lex = lexer.lexer(content)
    #Ahora  llamamos al metodo "tokenize"
    tokens = lex.tokenize(content)
    return json.dumps(tokens)
    #return tokens

#main()


if __name__ == '__main__':
    app.run(debug=True)
