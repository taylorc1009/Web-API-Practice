function helloFunction () {
	alert ('Hello Napier');
}

function getDateTime() {
	var dateTime = Date();
	document.getElementById('datetime').innerHTML = '<p>' + dateTime + '</p>';
}

function changeColour(obj, colour) {
	obj.style.color = colour;
}