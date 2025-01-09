/*
	Js functions for the doc project
*/

//Service the navbar search button
function search()
{
	searchterm = $('#searchvalue').val()
	window.find(searchterm,false,false,true)
}

