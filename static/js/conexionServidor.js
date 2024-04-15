const inputBox = document.getElementById("code-box");

inputBox.addEventListener('change', () =>{
    const content = inputBox.value;

    fetch('http://localhost:5000/lexer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({content: content})
    })
    .then(response => response.json())
    .then(data=>{
        console.log('Tokens', data.tokens);
    })
    .catch(error=>{
        console.error('Error al tokenizar las palabras: ', error)
    });
});