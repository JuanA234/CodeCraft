const inputBox = document.getElementById("code-box");


document.getElementById("btnEnviar").addEventListener('click', () =>{
    const content = inputBox.value;
//'http://localhost:5000/lexer'
//'https://codecraftbackend-ohlf.onrender.com/lexer'
    fetch('http://localhost:5000/lexer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin':'https://127.0.0.1:5000',
            'Access-Control-Credentials':'true'
        },
        body: JSON.stringify({content: content})
    })
    .then(response => response.json())
    .then(data=>{
        console.log('Tokens', data);
        const outputArea = document.getElementById('output-area');
        outputArea.value = JSON.stringify(data); // Aquí se establece el contenido del textarea
    })
    .catch(error=>{
        console.error('Error al tokenizar las palabras: ', error)
    });
});