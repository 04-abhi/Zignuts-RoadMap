function findFactorial(num) {
    if (num <= 1) {
        return 1;
    }
    return num * findFactorial(num - 1);
}

// Example
console.log("Factorial of 6 =", findFactorial(6));
