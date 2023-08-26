const express = require('express')
const app = express();
const port = 5000;

app.get('/', (req, res) => {
    res.sendFile('index.html', {root: __dirname});
});

app.listen(port, () => {
    console.log(`Now listening on port ${port}`);
});

document.addEventListener("DOMContentLoaded", function() {
    const image = document.querySelector(".fade-in");
    image.classList.add("fade-in");
});