// http://127.0.0.1:5000/webapp/address/0xd3cda913deb6f67967b99d67acdfa1712c293601
// http://127.0.0.1:5000/explorer/v1/address/0xd3cda913deb6f67967b99d67acdfa1712c293601

window.onload = function () {
	var url_frontend = (decodeURI(window.location.href));
	alert(url_frontend);

	var urlsplit = url_frontend.split("/");
	var url_split = urlsplit[5];
	alert(typeof url_split)
	
	var url_backend = 'http://127.0.0.1:5000/explorer/v1/address/%s', url_split;
	alert(url_backend);

	const xhr = new XMLHttpRequest();
	xhr.open('GET', url_backend, true);
	//xhr.responseType = 'json';
	xhr.send();
	xhr.onload = function() {
		let responseObj = xhr.response;
		console.log(responseObj); 
		
	  };
	  var data = 20;
	  buildUI(data);
  }

function buildUI(data) {
	for (var i = 0; i < data; ++i) {
		var p = document.createElement("p");
		p.innerText = "Asset " + i;
		document.getElementById("content").appendChild(p);
	}
}