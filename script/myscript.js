function validate(){
  pass = true;
  // if (validateName() == false) pass = false
  validatename();
  validatenametwo();
  validatenumber();
  return pass
}

// First name validation
function validatename(){
  var fail = true;
  var name = document.getElementById('name').value;
  var string=/^[a-zA-Z]+$/;

    if (!name.match(string))
    {
        alert("Must input string");
    }
  // var lettercheck = document.getElementById('name').value;

  if (name.length>10){
    alert('The first name is too long, please shorten to below 10 characters');
  }

  return false;
  // if (name.isInteger()){
  //   alert('No integers allowed in this field')
  // }
}

// Second name validation
function validatenametwo(){
  var fail = true;
  var lname = document.getElementById('lname').value;
  var string=/^[a-zA-Z]+$/;

    if (!lname.match(string))
    {
        alert("Must input string");
    }

  if (lname.length>10){
    alert('The last name is too long, please shorten to below 10 characters');
  }

  return false;

}

// function validatenumber()
// {
//     var fail = true;
//     var number=document.forms["myForm"]["number"].value;
//     if (isNaN(telephonenumber)) // this is the code I need to change
//     {
//         alert("Must input numbers");
//     }
//     return false;
// }

// number validation
function validatenumber(){

  var numbervalidate = document.forms["myForm"]["number"].value;

  if(!/^[0-9]+$/.test(numbervalidate)){
    alert("Please only enter numbers")
  }
}

function mySubmit() {
  console.log(document.forms["myForm"]);
  var commentadd = document.getElementById("comments").value;
  console.log(commentadd);
  var x = document.createElement("x");
  x.appendChild(document.createTextNode(commentadd));
  document.getElementById('newsArticle').appendChild(x);

}
//
// function stdSubmit() {
//   console.log('stdSubmit');
//   var commentadd = document.getElementById("comments").value;
//   var x = document.createElement("x");
//   x.appendChild(document.createTextNode(comments));
//   document.getElementById('newsArticle').appendChild(x);
//   alert('stdSubmit')
// }













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
