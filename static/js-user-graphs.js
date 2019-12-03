
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
          data: user1,
          label: "General experience (1-10)",
          borderColor: "#3e95cd",
          fill: false
        },
        {
          data: user2,
          label: "General experience (1-10)",
          borderColor: "#c45850",
          fill: false
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
