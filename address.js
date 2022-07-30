// http://127.0.0.1:5000/webapp/address/0xd3cda913deb6f67967b99d67acdfa1712c293601
// http://127.0.0.1:5000/explorer/v1/address/0xd3cda913deb6f67967b99d67acdfa1712c293601

window.onload = function () {
	const url_frontend = (decodeURI(window.location.href));
	const urlsplit = url_frontend.split("/");
	const url_split = urlsplit[5];
	const url_backend = 'http://127.0.0.1:5000/explorer/v1/address/' + url_split;

	// const xhr = new XMLHttpRequest();
	// xhr.open('GET', url_backend, true);
	// xhr.send();
	// xhr.onload = function () {
	// 	const responseObj = xhr.response;
	// 	buildUI(responseObj);
	// };

	const targetBlock = document.getElementById("content");

	const assetBlock1 = buildAssetUIBlock("MATIC", "Polygon", [
		{
			"blockchain": "Ethereum",
			"balance": null,
			"token": true,
			"alternatives": {
				"com.blockchain": "https://blockchair.com/ethereum/erc-20/token/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		},
		{
			"blockchain": "Polygon",
			"balance": null,
			"token": false,
			"alternatives": {
				"com.polygonscan": "https://polygonscan.com/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
				"io.explorer.bitquery": "https://explorer.bitquery.io/matic/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		}
	]);
	const assetBlock2 = buildAssetUIBlock("BUSD-T", "BUSD Token", [
		{
			"blockchain": "Binance Smart Chain",
			"balance": null,
			"token": true,
			"alternatives": {
				"com.bscscan": "https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		}
	]);

	targetBlock.appendChild(assetBlock1);
	targetBlock.appendChild(assetBlock2);
}

function buildUI(responseObj) {
	const p = document.createElement("p");
	p.innerText = responseObj;
	document.getElementById("content").appendChild(p);
}

function buildAssetUIBlock(assetCode, balance, blockchains) {
	const assetRowBlock = document.createElement("div");
	assetRowBlock.classList = "row asset-row";

	// TODO: Implement block
	assetRowBlock.innerText = "TODO: Implement block";

	return assetRowBlock;
}
