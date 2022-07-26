window.onload = function () {
	console.log("Hello, World 2 !!!");

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