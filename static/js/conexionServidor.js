const inputBox = document.getElementById("code-box");

inputBox.addEventListener('change', () =>{
    const content = inputBox.value;
    console.log(content);
//'http://localhost:5000/lexer'
//'https://codecraftbackend-ohlf.onrender.com/lexer'
    fetch('https://codecraftbackend-ohlf.onrender.com/lexer', {
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
    })
    .catch(error=>{
        console.error('Error al tokenizar las palabras: ', error)
    });
});