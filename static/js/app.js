// Install the onclick event in all news arrows the user did not voted already.
$(document).ready(function() {
    $('#parse').click(function() {
		alert('button clicked');	
	data = { 'url' : $('#url').val()  };
	$.ajax({
		   type: "POST",
		   url: "/api/addjob",
		   data: data,
		   success: function(msg){
			alert(msg);
		   }
	 });

    });
});
