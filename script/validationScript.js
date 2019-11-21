var username = document.getElementById("usernameInput").value;
var password = document.getElementById("passwordInput").value;

var lowerCaseLetters = /[a-z]/g;
var upperCaseLetters = /[A-Z]/g;
var numbers = /[0-9]/g;

if (username.value.match(lowerCaseLetters)) AND (username.value.match(upperCaseLetters))
