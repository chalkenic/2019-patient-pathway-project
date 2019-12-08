
$(document).ready(function() {


  // console.log(linegraph_data)
  // console.log(children)
  console.log(linegraph_data);

  var all_users_experiences = [];
  var start_date = linegraph_data [0][0][4];
  console.log("Start date: " + start_date);

  // console.log("Start date: " + start_date.getDate() + 1);

  survey_dates = [];

  for (var time_count = 0; time_count < Object.keys(linegraph_data[0]).length; time_count++) {
    var currDate = new Date(start_date);
    let formattedDate = currDate.getFullYear() + "-" + (currDate.getMonth()+1) + "-" + (currDate.getDate() + time_count);

    survey_dates.push(formattedDate);
  }

  // var helloDate = new Date(start_date);
  // helloDate.setDate(helloDate.getDate() + 1);
  // console.log(helloDate)

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
  console.log("All users in array: ")
  console.log(all_users_experiences)
  console.log("All data contained in array '0': ")
  console.log(all_users_experiences[0])
  console.log("all data contained in array '1': ")
  console.log(all_users_experiences[1])

  // for(sum_count = 0; sum_count < all_users_experiences[0].length; sum_count++) {
  //   console.log(sum_count)
  // }
  var total_users = Object.keys(linegraph_data).length;
  console.log(total_users)

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
  console.log("Initial list: "+ user_exp_aggregate);
  for (var i = 0; i < total_users.length; i++){
    user_exp_aggregate.push(all_users_experiences[0][i] + all_users_experiences[1][i]);
    console.log("updated list: " + user_exp_aggregate);
  }
  console.log("Total list: " + user_exp_aggregate);

  // for (var total_user_count = total_users; total_user_count > 0; total_user_count--) {
  //   // console.log("Hello" + total_user_count);
  //   var user_exp_totals = all_users_experiences.map((a, total_users) => a + all_users_experiences[total_users]);
  //   console.log(user_exp_totals);
  // }


    // console.log(pos_total)

  // for()


  var ctx = document.getElementById("line_graph");
  var line_graph = new Chart(ctx, {
    type: 'line',
    data: {
      labels: survey_dates,
      datasets: [

          {
          data: all_users_experiences[0],
          label: "User_1",
          borderColor: "#3e95cd",
          fill: false
        },
        {
          data: all_users_experiences[1],
          label: "User_2",
          borderColor: "#c45850",
          fill: false
        }
      ]
    }
  });

});
