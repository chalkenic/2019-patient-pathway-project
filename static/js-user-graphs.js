function demoFromHTML() {
    var pdf = new jsPDF('p', 'pt', 'letter');
    // source can be HTML-formatted string, or a reference
    // to an actual DOM element from which the text will be scraped.
    source = $('#content')[0];

    // we support special element handlers. Register them with jQuery-style
    // ID selector for either ID or node name. ("#iAmID", "div", "span" etc.)
    // There is no support for any other type of selectors
    // (class, of compound) at this time.
    specialElementHandlers = {
        // element with id of "bypass" - jQuery style selector
        '#bypassme': function (element, renderer) {
            // true = "handled elsewhere, bypass text extraction"
            return true
        }
    };
    margins = {
        top: 80,
        bottom: 60,
        left: 40,
        width: 522
    };
    // all coords and widths are in jsPDF instance's declared units
    // 'inches' in this case
    pdf.fromHTML(
        source, // HTML string or DOM elem ref.
        margins.left, // x coord
        margins.top, { // y coord
            'width': margins.width, // max width of content on PDF
            'elementHandlers': specialElementHandlers
        },

        function (dispose) {
            // dispose: object with X, Y of the last line add to the PDF
            //          this allow the insertion of new lines after html
            pdf.save('Test.pdf');
        }, margins
    );
}


$(document).ready(function() {



  console.log(linegraph_data);


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
            label: "Experience trendline",
            style: "rgb(43, 66, 255, 0.3)",
            lineStyle: "dotted|solid",
            width: 2
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

});
