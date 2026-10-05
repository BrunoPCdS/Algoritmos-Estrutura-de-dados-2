const prompt = require('prompt-sync')();

const numero = prompt("Digite um número inteiro: ");

let contador = 0;

for (const digito of numero) {
    if (Number(digito) % 2 === 0) {
        if (digito !== '0') {
            contador++;
        }
    }
}

console.log(`O número ${numero} possui ${contador} dígito(s) par(es).`);