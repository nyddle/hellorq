$(document).ready(function() {
    $('#parse').click(function() {
	alert('button clicked');	
	data = { 'url' : $('#url').val()  };
	$.ajax({
		   type: "POST",
		   url: "/api/addjob",
		   data: data,
		   success: function(msg){
			alert(JSON.stringify(msg));
		   }
	 });

    });
});

