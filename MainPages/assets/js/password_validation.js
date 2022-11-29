
var myInput = document.getElementById("password");
var letter = document.getElementById("letter");
var upper = document.getElementById("upper");
var num = document.getElementById("num");
var len = document.getElementById("len");

// When the user starts to type something inside the password field
myInput.onkeyup = function () {
    // Validate lowercase letters
    var lowerCaseLetters = /[a-z]/g;
    if (myInput.value.match(lowerCaseLetters)) {
        letter.classList.remove("invalid");
        letter.classList.add("valid");
    } else {
        letter.classList.remove("valid");
        letter.classList.add("invalid");
    }
    var upperCaseLetters = /[A-Z]/g;
    if (myInput.value.match(upperCaseLetters)) {
        upper.classList.remove("invalid");
        upper.classList.add("valid");
    } else {
        upper.classList.remove("valid");
        upper.classList.add("invalid");
    }
    var nums = /[0-9]/g;
    if (myInput.value.match(nums)) {
        num.classList.remove("invalid");
        num.classList.add("valid");
    } else {
        num.classList.remove("valid");
        num.classList.add("invalid");
    }
    var length = myInput.value.length

    if (length >= 8) {
        len.classList.remove("invalid");
        len.classList.add("valid");
    } else {
        len.classList.remove("valid");
        len.classList.add("invalid");
    }

}
var confirm_pass = document.getElementById("con_password");


function check_similar() {
    if (confirm_pass != myInput) {
        alert("Confirm password and password should be same");
        return false;
    }
}
