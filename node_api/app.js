const express = require('express');
const app = express();

app.get('/hola', (req, res) => {
    res.json({ mensaje: '¡Hola, mundo!' });
});

app.get('/hola/:nombre', (req, res) => {
    const nombre = req.params.nombre;
    res.json({ mensaje: `¡Hola, ${nombre}!` });
});

const PORT = 8002;
app.listen(PORT, () => {
    console.log(`Node.js API listening on port ${PORT}`);
});

