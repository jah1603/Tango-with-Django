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

$('#greetings').click(function(){
var userid;
userid = $(this).attr("data-userid");
$.get('/rango/greet_user/', {user_id: userid}, function(data){
$('#greet_count').html(data);
$('#greetings').hide();
});
});

});
