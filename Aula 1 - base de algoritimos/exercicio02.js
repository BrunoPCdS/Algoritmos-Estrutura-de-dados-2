
/*const prompt = require('prompt-sync')();

const texto = prompt("Digite uma palavra ou frase: ");

let resultado = "";

for (const letra of texto) {
    if (
        letra === "a" || letra === "e" || letra === "i" ||
        letra === "o" || letra === "u" ||
        letra === "A" || letra === "E" || letra === "I" ||
        letra === "O" || letra === "U"
    ) {
        resultado += "*";
    } else {
        resultado += letra;
    }
}

console.log(resultado); */



const prompt = require('prompt-sync')();

const texto = prompt("Digite uma palavra ou frase: ");

const resultado = texto.replace(/[aeiouAEIOU]/g, "*");

console.log(resultado);