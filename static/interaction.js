$( document ).ready(function() {
	$(".vote").mouseover(function() {
		var person = $(this).attr("title");
		$(".vote").css("opacity", "0.3");
		$(".name-"+person).css("opacity", "1.0");
		$(".name-"+person).css("border", "2px solid #222");
	});
	$(".vote").mouseout(function() {
		$(".vote").css("opacity", "1.0");
		$(".vote").css("border", "0");
	});
});