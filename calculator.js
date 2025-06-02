// Basic Calculator in JavaScript
function add(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

function multiply(a, b) {
    return a * b;
}

function divide(a, b) {
    if (b === 0) {
        throw new Error('Cannot divide by zero');
    }
    return a / b;
}

// Example usage:
console.log('Add: 2 + 3 =', add(2, 3));
console.log('Subtract: 5 - 2 =', subtract(5, 2));
console.log('Multiply: 4 * 3 =', multiply(4, 3));
console.log('Divide: 10 / 2 =', divide(10, 2));

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter the first number: ', (inputA) => {
    rl.question('Enter the second number: ', (inputB) => {
        const a = parseFloat(inputA);
        const b = parseFloat(inputB);
        if (isNaN(a) || isNaN(b)) {
            console.log('Invalid input. Please enter valid numbers.');
        } else {
            console.log('Add:', a, '+', b, '=', add(a, b));
            console.log('Subtract:', a, '-', b, '=', subtract(a, b));
            console.log('Multiply:', a, '*', b, '=', multiply(a, b));
            try {
                console.log('Divide:', a, '/', b, '=', divide(a, b));
            } catch (err) {
                console.log('Divide:', err.message);
            }
        }
        rl.close();
    });
});
