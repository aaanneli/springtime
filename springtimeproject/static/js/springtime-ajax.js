
$(document).ready(function(){

	$("#loadRadios").click(function(){
		console.log('fuck');
		var month = $("#id_date_month option:selected").text();
		var date = $("#id_date_day option:selected").text();
		var year = $("#id_date_year option:selected").text();
		$.get('/springtime/check_booking', {month:month, date:date, year:year},
			function(data){
				console.log(data)
			});
	});

});
