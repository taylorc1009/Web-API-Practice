function getDateTime() {
	if(window.confirm('Are you sure?')) { //confirmation prompt example
		var dateTime = Date();
		document.getElementById('datetime').innerHTML = '<p>' + dateTime + '</p>';
	}
}

function changeColour(obj, color) {
	obj.style.color = color;
}

function setCookie(name, value, expiry) {
	var d = new Date();

	d.setTime(d.getTime() + (expiry*24*60*60*1000));
	var expires = "expires="+ d.toUTCString();
	
	document.cookie = name + "=" + value + ";" + expires;
	return document.cookie;
}

function storeValue(name, value, storage) {
	try { //tries to store the data in storage (type may be either: session (temporary) or local (permanent))
		storage.setItem(name, value);
		return true;
	}
	catch (e) { //checks if storage didn't fail because it is full (returns true if it did)
		return e instanceof DOMException && (
		e.code === 22 ||
		e.code === 1014 ||
		e.name === 'QuotaExceededError' ||
		e.name === 'NS_ERROR_DOM_QUOTA_REACHED') &&
		storage.length !== 0;
	}
}

function removeValue(name, storage) {
	try {
		if(storage.getItem(name) !== null) {
			storage.removeItem(name);
			return true;
		}
		throw IllegalStateException;
	}
	catch(e) {
		return false;
	}
}