//Creamos los diccionarios

const conditionals = {
    "si":"if",
    "sino":"elif",
    "contrario":"else"
}


const operators = {
    "craftear":"sum",
    "desgastar":"substraction",
    "encantar":"multiplication",
    "desencantar":"division",
    "residuo":"module"
}

const variableType = {
    "bloque":"integer",
    "hiloRedstone":"string",
    "pasoHelado":"float",
    "booleanman":"boolean"
}

const logicOperators = {
    "interruptor":"And",
    "puerta":"or",
    "cierre":"not"
}

const controlStructures = {
    "minarPara":"for",
    "mientrasNoDiamante":"while",
    "picoRoto":"break",
    "seguirPicando":"continue"
}

//funcion para separar lineas de codigo

function splitString(stringToSplit, separator) {
    let arrayOfStrings = stringToSplit.split(separator);
  
    console.log("El codigo original es: ", stringToSplit);
    console.log("El separador es: ", separator);
    console.log(
      "El array tiene: ",
      arrayOfStrings.length,
      "elementos:",
      arrayOfStrings.join(" / "),
    );
    return arrayOfStrings
}

//Validamos la expresion regular

function validateExpression(code){
    let regExp = /\b\w+\b|\w+(?=\w)/g;
    let splitText = splitString(code, "\n");
    let output = "";
    splitText.forEach((linea, index) => {
        let words = linea.match(regExp);
        let lineOutput = "";
        if (words && words.length>0){
            words.forEach(word => {
                if (conditionals[word]) {
                    lineOutput += 'La palabra "' + word + '" es un condicional.\n';
                } else if (variableType[word]) {
                    lineOutput += 'La palabra "' + word + '" es un tipo de variable.\n';
                } else if (operators[word]) {
                    lineOutput += 'La palabra "' + word + '" es un operador.\n';
                } else if (logicOperators[word]) {
                    lineOutput += 'La palabra "' + word + '" es un operador lógico.\n';
                } else if (controlStructures[word]) {
                    lineOutput += 'La palabra "' + word + '" es una estructura de control.\n';
                } else{
                    lineOutput += 'La palabra "' + word + '" no se reconoce.\n';
                }
            });
        }
        if(words){
        lineOutput += (words.length > 1 ? 'Están ubicadas en la línea #' + (index + 1) + '\n\n' 
        : 'Está ubicada en la línea #' + (index + 1) + '\n\n');
        output += lineOutput;
        }
    });
    return output;
}
  
function validateCode(){
    var code = document.getElementById("code-box").value;
    var result = validateExpression(code);
    document.getElementById("output-area").innerHTML = result;
}