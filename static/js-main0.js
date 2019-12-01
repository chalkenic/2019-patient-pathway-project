// // function getCookie(name) {
// //   var cookieArr = document.cookie.split(";");
// //
// //   for (var i = 0; i <cookieArr.length; i++) {
// //     var cookiePair = cookieArr[i].split("=");
// //
// //     if (name == cookiePair[0].trim()) {
// //       return decodeURIComponent(cookiePair[1]);
// //     }
// //   }
// // }
//
// // document.write(getCookie("email_addr"))
//
//
// function callAjax(url)
// {
//   var xmlhttp = new XMLHttpRequest();
//
//   xmlhttp.onreadystatechange = function()
//   {
//     if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
//     {
//         var data = JSON.parse(xmlhttp.responseText);
//
//         document.getElementById("test").innerHTML = data.email_;
//     }
//   }
//   xmlhttp.open("GET", "line_graph_data.txt", true);
//   xmlhttp.send();
// }
//
// function cb_myCallback (theStuff)
// {
//   console.log(theStuff)
// }
$(document).ready(function() {


  console.log(data);

  // data.forEach(function(item, index){
  //   console.log(item, index);
  // });

  // data.forEach(function(item, index){
  //   console.log('Survey ID: '+ item[0]);
  //   console.log('General Happiness: '+ item[2]);
  //   console.log('Date: '+ item[3]);
  // });
  var time = []
  var gen_happ = []

  data.forEach(function(data){
  time.push(data[3])
  console.log(time);
  })

  data.forEach(function(data){
  gen_happ.push(data[2])
  console.log(time);
  })


  var ctx = document.getElementById("userChart");
  var userChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: time,
      datasets: [
        {
          data: gen_happ,
          label: "General experience (1-10)",
          borderColor: "#3e95cd",
          fill: false
        }
        //
        // {
        //   data: int_happ,
        //   label: "Interactional Happiness",
        //   borderColor: "#c45850",
        //   fill: false
        // }
      ]
    }
  });

});



// document.getElementById('all_patients').addEventListener('click', loadPatients);
//
// function loadPatients(){
//   var xhr = new XMLHttpRequest();
//   xhr.open('GET', 'accounts_data.json', true);
//
//   xhr.onload = function(){
//     if(this.status == 200){
//       var patients = JSON.parse(this.responseText);
//       console.log(patients)
//
//       var output = '';
//
//       for (var i in patients){
//         output += '<ul>' +
//           '<li>User ID: ' + patients[i].userID +'</li>' +
//           '<li>Email Address: ' + patients[i].email_addr +'</li>' +
//           '<li>Name: ' + patients[i].name +'</li>' +
//           '</ul>';
//
//       }
//
//       document.getElementById('patients').innerHTML = output;
//     }
//   }
//   xhr.send()
// }



// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
