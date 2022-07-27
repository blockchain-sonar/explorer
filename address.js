// http://127.0.0.1:5000/webapp/address/0xd3cda913deb6f67967b99d67acdfa1712c293601
// http://127.0.0.1:5000/explorer/v1/address/0xd3cda913deb6f67967b99d67acdfa1712c293601

window.onload = function () {
	const xhr = new XMLHttpRequest();
	xhr.open('GET', 'http://127.0.0.1:5000/webapp/address/%s', true);
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