
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
    let formattedDate = currDate.getFullYear() + "-" + (currDate.getMonth()+1) + "-" + (currDate.getDate() + time_count)
    console.log(formattedDate);

    console.log(time_count);
    survey_dates.push(formattedDate)
  }

  console.log(survey_dates)
  // var helloDate = new Date(start_date);
  // helloDate.setDate(helloDate.getDate() + 1);
  // console.log(helloDate)

  //Captures all experience data in
  for (var user_count = 0; user_count < Object.keys(linegraph_data).length; user_count++) {

    var user_data = Object.values(linegraph_data[user_count]);

    var user_data_in_survey = user_data.length;

    if(user_data_in_survey > 0){
      var user_experience_levels = [];
      console.log("User data " + user_count + ": " + user_data);
      for(var user_survey_count = 0; user_survey_count < user_data.length; user_survey_count++) {
        var user_survey_data = Object.values(user_data[user_survey_count]);
        // console.log(user_survey_data[2]);

        user_experience_levels.push(user_survey_data[2]);

      }
      console.log("experience_levels");
      console.log(user_experience_levels);
      all_users_experiences.push(user_experience_levels)
    }
    // console.log(experience_levels)
  }
  console.log(all_users_experiences)
  console.log(all_users_experiences[0])
  console.log(all_users_experiences[1])

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
  // console.log(linegraph_data.0);

  // const data_array = linegraph_data['items'][0]['name'];


  // var time = []
  // var gen_happ = []
  // var interactions = []
  //
  // var health = 0
  // var social_care = 0
  // var local_authority = 0
  // var third_sector = 0
  // var social = 0
  // var own_activities = 0


//   linegraph_data.forEach(function(linegraph_data){
//     time.push(linegraph_data[4])
//     console.log(time);
//   })
//
//   linegraph_data.forEach(function(linegraph_data){
//     gen_happ.push(linegraph_data[2])
//     console.log(gen_happ);
//   })
//
//   linegraph_data.forEach(function(linegraph_data){
//     interactions.push(linegraph_data[3])
//     console.log(interactions);
//   })
//
//   linegraph_data.forEach(function(linegraph_data){
//     if(linegraph_data[3] == "Health"){
//       health +=1;
//     }
//     else if(linegraph_data[3] == "Social Care"){
//       social_care +=1;
//     }
//     else if(linegraph_data[3] == "Local authority"){
//       local_authority +=1;
//     }
//     else if(linegraph_data[3] == "Third sector"){
//       third_sector +=1;
//     }
//     else if(linegraph_data[3] == "Social"){
//       social +=1;
//     }
//     else if(linegraph_data[3] == "Own activities"){
//       own_activities +=1;
//     }
//   })
//   console.log(health)
//
  // Adapted from Tobias Ahlin Bjerrome, 10 Chart.js example charts to get you started. Available at:
  // https://tobiasahlin.com/blog/chartjs-charts-to-get-you-started/
  // var ctx = document.getElementById("line_graph");
  // var line_graph = new Chart(ctx, {
  //   type: 'line',
  //   data: {
  //     labels: time,
  //     datasets: [
  //       {
  //         data: gen_happ,
  //         label: "General experience (1-10)",
  //         borderColor: "#3e95cd",
  //         fill: false
  //       }
  //     ]
  //   }
  // });
  //
  // var ctx = document.getElementById("bar_chart");
  // var bar_chart = new Chart(ctx, {
  //   type: 'bar',
  //   data: {
  //     labels: ["Health","Social Care","Local Authority","3rd Sector","Social","Own Activities"],
  //     datasets: [
  //       {
  //         data: [health,social_care,local_authority,third_sector,social,own_activities],
  //         label: "Interactions",
  //         backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#3e95cd"],
  //         borderColor: "#3e95cd",
  //         fill: false
  //       }
  //     ]
  //   },
  //   options: {
  //     legend: {display: false},
  //     title: {
  //       display: true,
  //       text: "Your interactions"
  //     }
  //   }
  // });
//
