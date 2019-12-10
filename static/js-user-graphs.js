// window.onload = function() {
//
// };
//
//


$(document).ready(function() {

  console.log(linegraph_data);
  console.log(table_data)

  var time = []
  var gen_happ = []
  var interactions = []

  var health = 0
  var social_care = 0
  var local_authority = 0
  var third_sector = 0
  var social = 0
  var own_activities = 0

  linegraph_data.forEach(function(linegraph_data){
    time.push(linegraph_data[4]);
  })

  linegraph_data.forEach(function(linegraph_data){
    gen_happ.push(linegraph_data[2]);
  })

  linegraph_data.forEach(function(linegraph_data){
    interactions.push(linegraph_data[3]);
  })

  linegraph_data.forEach(function(linegraph_data){
    if(linegraph_data[3] == "Health"){
      health +=1;
    }
    else if(linegraph_data[3] == "Social Care"){
      social_care +=1;
    }
    else if(linegraph_data[3] == "Local authority"){
      local_authority +=1;
    }
    else if(linegraph_data[3] == "Third sector"){
      third_sector +=1;
    }
    else if(linegraph_data[3] == "Social"){
      social +=1;
    }
    else if(linegraph_data[3] == "Own activities"){
      own_activities +=1;
    }
  })

  // Adapted from Tobias Ahlin Bjerrome, 10 Chart.js example charts to get you started. Available at:
  // https://tobiasahlin.com/blog/chartjs-charts-to-get-you-started/

  var user1 = [4,6,4,7,9,7];
  var user2 = [3,9,1,8,3,9];

  var ctx = document.getElementById("line_graph");
  var line_graph = new Chart(ctx, {
    type: 'line',
    data: {
      labels: time,
      datasets: [
        {
          data: gen_happ,
          label: "General experience (1-10)",
          borderColor: "#3e95cd",
          fill: false,
          trendlineLinear: {
            style: "rgba(119,136,153)",
            lineStyle: "dotted",
            width: 3
          }

        }
      ]
    }
  });

  var ctx = document.getElementById("bar_chart");
  var bar_chart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ["Health","Social Care","Local Authority","3rd Sector","Social","Own Activities"],
      datasets: [
        {
          data: [health,social_care,local_authority,third_sector,social,own_activities],
          label: "Interactions",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#3e95cd"],
          borderColor: "#3e95cd",
          fill: false
        }
      ]
    },
    options: {
      legend: {display: false},
      title: {
        display: true,
        text: "Your interactions"
      }
    }
  });

  // var canvas = document.getElementById('message_list');
  // var ctx = canvas.getContext('2d');
  //
  // var date

  var volunteer_name = linegraph_data[0][6];
  console.log(volunteer_name)

  document.getElementById('downloadPDF').addEventListener('click', downloadPDF);

  //Adapted from Rodrigo jsfiddle code for implementing chartJS data, available at: https://jsfiddle.net/crabbly/kL68ey5z/
  function downloadPDF() {
    var lineGraph = document.querySelector('#line_graph');
    var barChart = document.querySelector('#bar_chart');
    var messages = document.querySelector('#message_list');
    var elementHandlers = {
      '#ignorePDF': function(element, renderer) {
        return true;
      }
    };

    var lineGraphCanvas = lineGraph.toDataURL("image/png", 1.0);
    var barChartCanvas = barChart.toDataURL("image/png", 1.0);
    // var messageBoxCanvas = messages.toDataURL("image/png", 1.0);

    var doc = new jsPDF('p','mm', 'a4');

    var pageHeight = doc.internal.pageSize.height;

    doc.setFont("Courier")
    doc.setFontSize(20);
    doc.setFontType("Bold");
    doc.text(75, 15, "Volunteer #" + user_data + " - " + volunteer_name);

    doc.fromHTML($('#graph_header_1').html(), 10, 15, {
      'width': 190,
    'elementHandlers': elementHandlers
    });
    doc.addImage(lineGraphCanvas, 'PNG', 10, 30, 190, 100);

    doc.fromHTML($('#graph_header_2').html(), 10, 140, {
      'width': 190,
    'elementHandlers': elementHandlers
    });

    doc.addImage(barChartCanvas, 'PNG', 10, 155, 190, 100);

    doc.addPage()

    doc.fromHTML($('#user_messages').html(), 10, 10, {
      'width': 190,
    'elementHandlers': elementHandlers
    });

    margins = {
      top: 20,
      bottom: 20,
      left: 30,
      width: 190,
    };

    doc.fromHTML($('#message_list')[0], margins.left, margins.top, {
      'width': margins.width,
      'elementHandlers': elementHandlers
    });

    // doc.addImage(messageBoxCanvas, 'PNG', 10, 155, 190);

    doc.save("Volunteer " + user_data + " data.pdf");

  }

});
