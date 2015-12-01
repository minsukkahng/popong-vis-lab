$( document ).ready(function() {
	$(".vote").mouseenter(function() {
		var person = $(this).attr("title");
		$(".vote").css("opacity", "0.3");
		$(".name-"+person).css("opacity", "1.0");
		$(".name-"+person).css("border", "2px solid #222");
	})
	.mouseleave(function() {
		$(".vote").css("opacity", "1.0");
		$(".vote").css("border", "0");
	});

	$("#person-list li").mouseenter(function() {
		var person = $(this).attr("data-person");
		$(this).find("span").css("background-color", "#99f");
		$(".vote").css("opacity", "0.3");
		$(".name-"+person).css("opacity", "1.0");
		//$(".name-"+person).css("border", "2px solid #222");
	})
	.mouseleave(function() {
		$(this).find("span").css("background-color", "#eee");
		$(".vote").css("opacity", "1.0");
		//$(".vote").css("border", "0");
	});
});