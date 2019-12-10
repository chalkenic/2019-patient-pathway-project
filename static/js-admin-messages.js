function deleteMessage(messageID){
  console.log(messageID);
  confirm = confirm("Really delete?");

  if (confirm == true){
    $.ajax('/deleteMsg', {
      type: 'DELETE',
      data: {
        id: messageID
      },
      success: function(){
        console.log("Success");
      },

      error: function() {
        console.log("Error when deleting message.");
      }
    });
  }
  return false;
};

$(document).ready(function() {
  $("#rowClick > tr").click(function(){
      $(this).toggleClass("active");
  });
});
