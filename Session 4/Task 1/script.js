function getSum(event) {
    var inputString = document.getElementById("inpString").value;
    var result = 0;
    if (event) event.preventDefault();
    for (let index = 0; index < inputString.length; index++) {
        // checking if the char is a number
        if (inputString.charCodeAt(index) >= 48 && inputString.charCodeAt(index) <= 57) {
            result += inputString.charCodeAt(index) - 48;
        }
        
    }
    if (result == 0) {
        console.log("No numbers in the string");
    } else {
        console.log("The sum of the numbers in the string is " + result);
        // displaying the output in P tag
        document.getElementById("result").innerHTML = "Sum:" + result;
    }
}