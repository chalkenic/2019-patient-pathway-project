// function ChangeBrand() {
//   var xhttp = new XMLHttpRequest();
//   xhttp.open("GET", '/home', true);
//   xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//
//   xhttp.onreadystatechange = function() {
//     if (xhttp.readyState === 4) {
//       if (xhttp.status === 200) {
//         // var text = "Admin"
//         var text = xhttp.responseText
//         document.getElementById("user").innerHTML = text;
//       } else {
//         console.error(xhttp.statusText);
//       }
//     }
//   };
//   xhttp.send()
// };

// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF

var time = [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050];
// For drawing the lines
var gen_happ = [86,114,106,106,107,111,133,221,783,2478];
var int_happ = [6,3,2,2,7,26,82,172,312,433];

var ctx = document.getElementById("userChart");
var userChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: time,
    datasets: [
      {
        data: gen_happ,
        label: "General happiness",
        borderColor: "#3e95cd",
        fill: false
      },

      {
        data: int_happ,
        label: "Interactional Happiness",
        borderColor: "#c45850",
        fill: false
      }
    ]
  }
});
