cardRegex = 0;
let isValid = false;

let mastercardRegex = /^(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))$/;
let visaRegex = /^4[0-9]{12}(?:[0-9]{3})?$/;
let amexRegex = /^3[47][0-9]{13}$/;

function selectCard(value) { 
    console.log(value);
    if (value === "amex") {
        cardRegex = amexRegex;
    } else if (value == "visa") {
        cardRegex == visaRegex;
    } else if (value == "mc") {
        cardRegex = mastercardRegex;
    }
    console.log(cardRegex);
}

function checkRegex() {
    const value = document.getElementById('ccnum').value;
    console.log(cardRegex);
    console.log(value);
    console.log(cardRegex.test(value));
    if (cardRegex.test(value)) {
        isValid = true;
    } else {
        isValid = false;
    }

    if(!isValid) {
         alert("Please provide a valid card number!");
    }
}

function checkDate(){
    //update value every run
    var expiry_month = document.getElementById("expireMM").value;
    var expiry_year = document.getElementById("expireYY").value;
    
    var today = new Date();
    var selDate = new Date();
    console.log("check");
    if (today.getTime() > selDate.setFullYear(expiry_year, expiry_month)){
        console.log("check");
        alert ("Expiry month and year is before today month and year.");
        return false;
    }
}
