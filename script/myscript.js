function validate() {
  pass = true;
  // if (validateName() == false) pass = false
  validatename();
  validatenametwo();
  return pass
}

// First name validation
function validatename() {
  var fail = true;
  var name = document.getElementById('name').value;
  var string = /^[a-zA-Z]+$/;

  if (!name.match(string)) {
    alert("Must input string");
  }
  // var lettercheck = document.getElementById('name').value;

  if (name.length > 10) {
    alert('The first name is too long, please shorten to below 10 characters');
  }

  return false;
  // if (name.isInteger()){
  //   alert('No integers allowed in this field')
  // }
}

// Second name validation
function validatenametwo() {
  var fail = true;
  var lname = document.getElementById('lname').value;
  var string = /^[a-zA-Z]+$/;

  if (!lname.match(string)) {
    alert("Must input string");
  }

  if (lname.length > 10) {
    alert('The last name is too long, please shorten to below 10 characters');
  }

  return false;

}



// function validatenumber() {

//   var numbervalidate = document.forms["myForm"]["number"].value;

//   if (!/^[0-9]+$/.test(numbervalidate)) {
//     alert("Please only enter numbers")
//   }
// }

// function mySubmit() {
//   console.log(document.forms["myForm"]);
//   var commentadd = document.getElementById("comments").value;
//   console.log(commentadd);
//   var x = document.createElement("x");
//   x.appendChild(document.createTextNode(commentadd));
//   document.getElementById('newsArticle').appendChild(x);

// }
// //
function stdSubmit() {
  console.log('stdSubmit');
  var commentadd = document.getElementById("comments").value;
  var x = document.createElement("x");
  x.appendChild(document.createTextNode(comments));
  document.getElementById('newsArticle').appendChild(x);
  alert('stdSubmit')
}

// FAQ CODE
var coll = document.getElementsByClassName("collapsible-faq");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight) {
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}











// function validate(){
//   pass = false
//   if (validateName() = false) pass = false
//   if (validatenametwo() = false) pass = false
//     function validatenametwo(){
//       var fail = true;
//       var name = document.getElementById('lname').value;
//       if (name.length>10){
//         alert('The last name is too long, please shorten to below 10 characters');
//       }
//       function validate(){
//         var fail = true;
//         var name = document.getElementById('name').value;
//         if (name.length>10){
//           alert('The first name is too long, please shorten to below 10 characters');
//         }


//   return pass
// }


// function validate(){
//   pass = false
//   if (validateName() == false) pass = false
//   if (validatenametwo() == false) pass = false
//   return pass
// }
//     function validatenametwo(){
//       var fail = true;
//       var name = document.getElementById('lname').value;
//       if (name.length>10){
//         alert('The last name is too long, please shorten to below 10 characters');
//       }
//       function validateName(){
//         var fail = true;
//         var name = document.getElementById('name').value;
//         if (name.length>10){
//           alert('The first name is too long, please shorten to below 10 characters');
//         }
// }
