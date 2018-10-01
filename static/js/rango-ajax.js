$(document).ready(function() {
// JQuery code to be added in here.
$('#likes').click(function(){
var userid;
userid = $(this).attr("data-userid");
$.get('/rango/like_user/', {user_id: userid}, function(data){
$('#like_count').html(data);
$('#likes').hide();
});
});
});
