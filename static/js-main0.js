// function getCookie(name) {
//   var cookieArr = document.cookie.split(";");
//
//   for (var i = 0; i <cookieArr.length; i++) {
//     var cookiePair = cookieArr[i].split("=");
//
//     if (name == cookiePair[0].trim()) {
//       return decodeURIComponent(cookiePair[1]);
//     }
//   }
// }

// document.write(getCookie("email_addr"))


function callAjax(url)
{
  var xmlhttp = new XMLHttpRequest();

  xmlhttp.onreadystatechange = function()
  {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
    {
        var data = JSON.parse(xmlhttp.responseText);

        document.getElementById("test").innerHTML = data.email_addr;
    }
  }
  xmlhttp.open("GET", "line_graph_data.txt", true);
  xmlhttp.send();
}

function cb_myCallback (theStuff)
{
  console.log(theStuff)
}

// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF
// TEST STUFF

// For drawing the lines
var gen_happ = l_values;
var int_happ = [6,3,2,2,7,26,82,172,312,433];

var ctx = document.getElementById("userChart");
var userChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [{% for item in l_labels %}
      "{{item}}",
      {% endfor %}]
    datasets: [
      {
        data: {{"1_values"}},
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
