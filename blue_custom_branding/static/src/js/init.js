// Load custom branding theme colors, if present.
$(document).ready(function() {
	$.get('/blue_custom_branding/cssClassname').then(function(res) {
		var jsonresult = JSON.parse(res);
		$('body').addClass(jsonresult.className);
	});
});
