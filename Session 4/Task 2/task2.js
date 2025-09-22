function addNumbersFromString(text) {
    let parts = text.split(",");   // break string into pieces
    let total = 0;
    for (let piece of parts) {
        total += Number(piece.trim());  // convert and add
    }
    return total;
}

// Example check
let values = "1.5, 2.3, 3.1, 4, 5.5, 6, 7, 8, 9, 10.9";
console.log("Total sum =", addNumbersFromString(values));
