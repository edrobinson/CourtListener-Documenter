/*
	Js functions for the doc project
*/

//Service the navbar search button
function search()
{
	searchterm = $('#searchvalue').val()
	window.find(searchterm,false,false,true)
}

//Load a page - see dropdown in the navbar
function showPage(path)
{
	location.replace(path)
}

