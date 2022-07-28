// http://127.0.0.1:5000/webapp/address/0xd3cda913deb6f67967b99d67acdfa1712c293601
// http://127.0.0.1:5000/explorer/v1/address/0xd3cda913deb6f67967b99d67acdfa1712c293601

window.onload = function () {
	var url_frontend = (decodeURI(window.location.href));
	var urlsplit = url_frontend.split("/");
	var url_split = urlsplit[5];

	var url_backend = 'http://127.0.0.1:5000/explorer/v1/address/' + url_split;

	const xhr = new XMLHttpRequest();
	xhr.open('GET', url_backend, true);
	//xhr.responseType = 'json';
	xhr.send();
	xhr.onload = function() {
		var responseObj = xhr.response;
		
		console.log(responseObj); 
		var p = document.createElement("p");
		p.innerHTML = responseObj;
		document.getElementById("content").appendChild(p);
		
	  };
	 
  }


		
	

  