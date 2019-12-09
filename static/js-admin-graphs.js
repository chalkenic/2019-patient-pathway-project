

$(document).ready(function() {


  // console.log(linegraph_data)
  // console.log(children)
  console.log(linegraph_data);

  var all_users_experiences = [];
  var start_date = "2019-11-1";
  // var start_date = linegraph_data [0][0][4];
  console.log("Start date: " + start_date);

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
      console.log("experience_levels");
      console.log(user_experience_levels);
      all_users_experiences.push(user_experience_levels)
    }
    // console.log(experience_levels)
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

        console.log("Data: " +user_survey_data)

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
      console.log("experience_levels");
      console.log(user_experience_levels);
      all_users_experiences.push(user_experience_levels);
    }
  };



  // console.log("All users in array: ")
  // console.log(all_users_experiences)
  // console.log("All data contained in array '0': ")
  // console.log(all_users_experiences[0])
  // console.log("all data contained in array '1': ")
  // console.log(all_users_experiences[1])

  // for(sum_count = 0; sum_count < all_users_experiences[0].length; sum_count++) {
  //   console.log(sum_count)
  // }
  // console.log(linegraph_data)
  var data_total = all_users_experiences[0].length;

  var user_total = Object.keys(linegraph_data).length;
    // var total_users = 30;
  console.log('total users: ' + user_total)
  console.log('Total data: ' + data_total)

  //
  // $scope.sum = function(items, prop) {
  //   if items.reduce(fucntion(a, b) {
  //     return a + b[prop];
  //   }, 0);
  // };
  //
  // $scope.travelerTotal = $scope.sum()

  // var sum = all_users_experiences.map(function (num, idx) {
  //   return num + all_users_experiences[idx];
  // });
  // console.log(sum)

  user_exp_aggregate = [];
  // console.log(all_users_experiences)
  console.log("Initial list: "+ user_exp_aggregate);
  for (var user = 0; user < user_total; user++){

    for(var data_item = 0; data_item < data_total; data_item++){}

    user_exp_aggregate.push(all_users_experiences[0][user] + all_users_experiences[1][user]);
    console.log("updated list: " + user_exp_aggregate);
  }
  console.log("Total list: " + user_exp_aggregate);

  // for (var total_user_count = total_users; total_user_count > 0; total_user_count--) {
  //   // console.log("Hello" + total_user_count);
  //   var user_exp_totals = all_users_experiences.map((a, total_users) => a + all_users_experiences[total_users]);
  //   console.log(user_exp_totals);
  // }

  var ctx = document.getElementById("line_graph");
  var line_graph = new Chart(ctx, {
    type: 'line',
    data: {
      labels: survey_dates,
      datasets: [{
          data: user_exp_aggregate,
          label: "Average",
          borderColor: "#c45850",
          fill: false,
          trendlineLinear: {
            label: "Experience trendline",
            borderColor: "#c45850",
            style: "rgb(43, 66, 255, 0.3)",
            lineStyle: "dotted|solid",
            width: 2
          }
        }
      ]
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

  // function getRandomColor() {
  //
  //   var colors = Array['#fc0000', '#0004ff', '#07fa02', '#e6f202' ];
  //   var color_choice = colors[Math.floor(Math.random()*color.length)];
  //   return color_choice;
  // }
  //

  function addData(chart, label, color, data) {
    chart.data.datasets.push({
      label: label,
      borderColor: color,
      data: data,
      fill: false
    });
    chart.update()}

  for(user = 0; user < user_total; user++){
    addData(line_graph, "user " + user, getRandomColor(), all_users_experiences[user]);

  };

  function deleteLast() {
    line_graph.data.datasets.pop();
    line_graph.update()
  }

  deleteLast()

});


function deleteUser(userID){
  console.log(userID);
  confirm = confirm("Really delete?");

  if (confirm == true){
    $.ajax('/delete', {
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
