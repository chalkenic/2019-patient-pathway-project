function ChangeBrand() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", '/home', true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

  xhttp.onreadystatechange = function() {
    if (xhttp.readyState === 4) {
      if (xhttp.status === 200) {
        // var text = "Admin"
        var text = xhttp.responseText
        document.getElementById("user").innerHTML = text;
      } else {
        console.error(xhttp.statusText);
      }
    }
  };
  xhttp.send()
};
