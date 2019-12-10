function deleteUser(userID){
  console.log(userID);
  confirm = confirm("Really delete?");

  if (confirm == true){
    $.ajax('/deleteUser', {
      type: 'DELETE',
      data: {
        id: userID
      },
      success: function(){
        console.log("Success");
      },

      error: function() {
        console.log("Error when deleting user.");
      }
    });
  }
  return false;
};

$(document).ready(function() {



  // console.log(linegraph_data)
  // console.log(children)
  console.log(linegraph_data);

  var all_users_experiences = [];
  var start_date = "2019-11-1";
  // var start_date = linegraph_data [0][0][4];
  // console.log("Start date: " + start_date);

  // console.log("Start date: " + start_date.getDate() + 1);

  survey_dates = [];

  var health = 0
  var social_care = 0
  var local_authority = 0
  var third_sector = 0
  var social = 0
  var own_activities = 0


  Object.keys(linegraph_data).forEach((key) => (linegraph_data[key] == null) && delete linegraph_data[key]);

  for (var time_count = 0; time_count < Object.keys(linegraph_data[0]).length; time_count++) {
    var currDate = new Date(start_date);
    let formattedDate = currDate.getFullYear() + "-" + (currDate.getMonth()+1) + "-" + (currDate.getDate() + time_count);

    survey_dates.push(formattedDate);
  }


  //Creates for loop with length based upon number of user IDs parsed from database.
  for (var user_count = 0; user_count < Object.keys(linegraph_data).length; user_count++) {

    //Variable that stores all values of user at dictionary & for loop position
    var user_data = Object.values(linegraph_data[user_count]);

    //Calculates length of data to check if any data present.
    var user_data_in_survey = user_data.length;

    //Confirms if user is administrator or user, and ignores if no entries available (i.e. admin)
    if(user_data_in_survey > 0){

      //Emppty list for storing future data provided in nested for loop.
      var user_experience_levels = [];

      //For loop criteria that checks all user's survey entries.
      for(var user_survey_count = 0; user_survey_count < user_data.length; user_survey_count++) {

        //Variable that stores all values of user at nested dictionary position.
        var user_survey_data = Object.values(user_data[user_survey_count]);

        //Pushes all value data at position 2 - the user experience.
        user_experience_levels.push(user_survey_data[2]);

      }
      all_users_experiences.push(user_experience_levels)
    }
  }

  //Creates for loop with length based upon number of user IDs parsed from database.
  for (var user_count = 0; user_count < Object.keys(linegraph_data).length; user_count++) {

    //Variable that stores all values of user at dictionary & for loop position
    var user_data = Object.values(linegraph_data[user_count]);

    //Calculates length of data to check if any data present.
    var user_data_in_survey = user_data.length;

    //Confirms if user is administrator or user, and ignores if no entries available (i.e. admin)
    if(user_data_in_survey > 0){

      //Emppty list for storing future data provided in nested for loop.
      var user_experience_levels = [];

      //For loop criteria that checks all user's survey entries.
      for(var user_survey_count = 0; user_survey_count < user_data.length; user_survey_count++) {

        //Variable that stores all values of user at nested dictionary position.
        var user_survey_data = Object.values(user_data[user_survey_count]);

        //Pushes all value data at position 2 - the user experience.
        if(user_survey_data[3] == "Health"){
          health +=1;
        }
        else if(user_survey_data[3] == "Social Care"){
          social_care +=1;
        }
        else if(user_survey_data[3] == "Local authority"){
          local_authority +=1;
        }
        else if(user_survey_data[3] == "Third sector"){
          third_sector +=1;
        }
        else if(user_survey_data[3] == "Social"){
          social +=1;
        }
        else if(user_survey_data[3] == "Own activities"){
          own_activities +=1;
        }

      }
      all_users_experiences.push(user_experience_levels);
    }
  };
  var data_total = all_users_experiences[0].length;

  var user_total = Object.keys(linegraph_data).length;


  var aggregate_total = user_total

  console.log('total users: ' + aggregate_total)
  console.log('Total individal user data points: ' + data_total)
  console.log("")
  console.log("Health interactions: " + health);
  console.log("social_care interactions: " + social_care);
  console.log("local_authority interactions: " + local_authority);
  console.log("third_sector interactions: " + third_sector);
  console.log("social interactions: " + social);
  console.log("own_activities interactions: " + own_activities);
  console.log("")


  var user_exp_aggregate = [];

  for (var entry = 0; entry < data_total; entry++){
    user_exp_aggregate[entry] = 0;
  }

  console.log("Checking total patient count...")
  console.log("")
  //For loop that selects all
  for (var user = 0; user < user_total; user++){

    for(var data_item = 0; data_item < data_total; data_item++){
      console.log("Checking user " + user + ": " + all_users_experiences[user])

      if(isNaN(all_users_experiences[user][2])){
        aggregate_total -- ;
        console.log("Null user found, removing from data. New aggregate total: " + aggregate_total)
        break;
      }
      else{
        user_exp_aggregate[data_item] = user_exp_aggregate[data_item] + all_users_experiences[user][data_item];
      }
    }
  }

  console.log('Final user count: ' + aggregate_total)




  for (var avg = 0; avg < user_exp_aggregate.length; avg++) {

    user_exp_aggregate[avg] = user_exp_aggregate[avg] / aggregate_total;
  };
  console.log("")
  console.log("Average data points: " + user_exp_aggregate);

  var ctx = document.getElementById("line_graph");
  var line_graph = new Chart(ctx, {
    type: 'line',
    data: {
      labels: survey_dates,
      datasets: [{
        data: user_exp_aggregate,
        label: "Average of all users",
        borderColor: "#000",
        borderDash: [10,5],
        // fill: false,
        trendlineLinear: {
          style: "rgba(119,136,153)",
          lineStyle: "dotted",
          width: 3
          }
      }]
    }
  });

  var ctx = document.getElementById("bar_chart");
  var bar_chart = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ["Health","Social Care","Local Authority","3rd Sector","Social","Own Activities"],
      datasets: [
        {
          data: [health,social_care,local_authority,third_sector,social,own_activities],
          label: "Interactions",
          backgroundColor: ["#9b00d4", "#ff0000","#0048ff","#07d400","#cdd400","#00bf8c"],
          borderColor: "#000",
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

//Code adapted from Flivni jsfiddle.net example - Add Dataset example. available at: https://jsfiddle.net/flivni/Lcnj1e5x/
  function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var color_pos = 0; color_pos < 6; color_pos++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  function addData(chart, label, color, data) {
    chart.data.datasets.push({
      label: label,
      borderColor: color,
      data: data,
      fill: false
    });
    chart.update()};

  for(user = 0; user < user_total; user++){
    addData(line_graph, "user " + (user + 1), getRandomColor(), all_users_experiences[user]);

  };

  function deleteLast() {
    line_graph.data.datasets.pop();
    line_graph.update()
  }
  deleteLast()

});
