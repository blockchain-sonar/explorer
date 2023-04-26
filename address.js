// http://127.0.0.1:5000/webapp/address/0xd3CdA913deB6f67967B99D67aCDFa1712C293601
// http://127.0.0.1:5000/explorer/v1/address/0xd3CdA913deB6f67967B99D67aCDFa1712C293601

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

	// Хардкодимо відповіть від сервера
	// Важаємо, що дані responseObj отримані с бекенду
	const responseObj = {
		"address": "0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
		"assets": {
			"BNB": {
				"alternatives": {
					"com.bscscan": "https://bscscan.com/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
					"io.binance.mintscan": "https://binance.mintscan.io/account/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
					"io.etherscan": "https://etherscan.io/token/0xB8c77482e45F1F44dE1745F52C74426C631bDD52?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
					"io.explorer.bitquery": "https://explorer.bitquery.io/bsc/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
				},
				"balance": null,
				"blockchains": [
					{
						"blockchain": "Binance Smart Coin",
						"token": false
					},
					{
						"blockchain": "Ethereum",
						"token": true
					}
				],
				"name": "Binance Coin"
			},
			"BUSD-T": {
				"alternatives": {
					"com.bscscan": "https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
					"io.explorer.bitquery": "https://explorer.bitquery.io/bsc/token/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
				},
				"balance": null,
				"blockchains": [
					{
						"blockchain": "Ethereum",
						"token": true
					}
				],
				"name": "BUSD Token"
			},
			"ETH": {
				"alternatives": {
					"com.bscscan": "https://bscscan.com/token/0x2170ed0880ac9a755fd29b2688956bd959f933f8?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
					"io.etherscan": "https://etherscan.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
					"io.ethplorer": "https://ethplorer.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
					"org.etherchain": "https://etherchain.org/account/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
				},
				"balance": null,
				"blockchains": [
					{
						"blockchain": "Ethereum",
						"token": false
					},
					{
						"blockchain": "Binance Smart Coin",
						"token": true
					}
				],
				"name": "Ether"
			},
			"MATIC": {
				"alternatives": {
					"com.blockchain": "https://blockchair.com/ethereum/erc-20/token/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
					"com.polygonscan": "https://polygonscan.com/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
					"io.explorer.bitquery": "https://explorer.bitquery.io/matic/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
				},
				"balance": null,
				"blockchains": [
					{
						"blockchain": "Ethereum",
						"token": true
					},
					{
						"blockchain": "Polygon",
						"token": false
					}
				],
				"name": "Polygon"
			},
			"USDT": {
				"alternatives": {
					"io.etherscan": "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
					"io.ethplorer": "https://ethplorer.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
					"org.etherchain": "https://etherchain.org/account/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
					"org.tronscan": "https://tronscan.org/#/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e/"
				},
				"balance": null,
				"blockchains": [
					{
						"blockchain": "Ethereum",
						"token": true
					},
					{
						"blockchain": "Tron",
						"token": true
					}
				],
				"name": "Tether"
			}
		}
	};

	// Конвертуємо дані з сервера в дані для для побудови UI
	const uiDataAssets = serverDataAssetsMapper(responseObj);

	// Будуємо UI блоки по кожному Asset
	const targetBlock = document.getElementById("content");
	for(const uiDataAsset of uiDataAssets) {
		const assetCode = uiDataAsset.assetCode;
		const assetName = uiDataAsset.assetName;
		const blockchains = uiDataAsset.blockchains;

		const assetBlock = buildAssetUIBlock(assetCode, assetName, blockchains);
	
		targetBlock.appendChild(assetBlock);
	}
}

function serverDataAssetsMapper(serverData) {
	const uiDataAssets = [];

	const asset0 = {
		assetCode: "USDT",
		assetName: "Tether (USDT)",
		blockchains: [
			{
				"blockchain": "Ethereum",
				"balance": "42042.766477",
				"token": true,
				"alternatives": {
					"io.etherscan": "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7?a=0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
					"io.ethplorer": "https://ethplorer.io/address/0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
					"org.etherchain": "https://etherchain.org/account/0xd3CdA913deB6f67967B99D67aCDFa1712C293601"
				}
			},
		]
	};

	const asset1 = {
		assetCode: "MATIC",
		assetName: "Polygon Coin",
		blockchains: [
			{
				"blockchain": "Ethereum",
				"balance": null,
				"token": true,
				"alternatives": {
					"io.etherscan": "https://etherscan.io/token/0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0?a=0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
					"io.ethplorer": "https://ethplorer.io/address/0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
					"org.etherchain": "https://etherchain.org/account/0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
					"com.blockchain": "https://blockchair.com/ethereum/erc-20/token/0xd3CdA913deB6f67967B99D67aCDFa1712C293601"
				}
			},
			{
				"blockchain": "Polygon",
				"balance": null,
				"token": false,
				"alternatives": {
					"com.polygonscan": "https://polygonscan.com/address/0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
					"io.explorer.bitquery": "https://explorer.bitquery.io/matic/address/0xd3CdA913deB6f67967B99D67aCDFa1712C293601"
				}
			}
		]
	};

	const asset2 = {
		assetCode: "BUSD-T",
		assetName: "BUSD Token",
		blockchains: [
			{
				"blockchain": "Binance Smart Chain",
				"balance": "100",
				"token": true,
				"alternatives": {
					"com.bscscan": "https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
				}
			}
		]
	}

	uiDataAssets.push(asset0);
	uiDataAssets.push(asset1);
	uiDataAssets.push(asset2);

	// TODO
	// Використовуючи дані serverData будуемо
	// набор assetData та додаємо в масив uiDataAssets
	// як в прикладі вище
	//


	return uiDataAssets;
}

function buildUI(responseObj) {
	const p = document.createElement("p");
	p.innerText = responseObj;
	document.getElementById("content").appendChild(p);
}

function buildAssetRootUIBlock() {
	const assetRowBlock = document.createElement("div");
	assetRowBlock.classList = "row asset-row";
	return assetRowBlock;
}

function buildAssetRootColBlock() {
	const assetRowColBlock = document.createElement("div");
	assetRowColBlock.classList = "col-12";
	return assetRowColBlock;
}

function buildAssetRootCardBlock() {
	const assetRootCardBlock = document.createElement("div");
	assetRootCardBlock.classList = "card";
	return assetRootCardBlock;
}

function buildAssetRootCardHeaderBlock() {
	const assetRootCardHeaderBlock = document.createElement("div");
	assetRootCardHeaderBlock.classList = "card-header";
	return assetRootCardHeaderBlock;
}

function buildAssetUIBlock(assetCode, balance, blockchains) {
	const assetRowRootBlock = buildAssetRootUIBlock();

	const assetRowRootColBlock = buildAssetRootColBlock();
	assetRowRootBlock.appendChild(assetRowRootColBlock);

	const assetRowCardRootBlock = buildAssetRootCardBlock();
	assetRowRootColBlock.appendChild(assetRowCardRootBlock);

	const assetRowRootCardHeaderBlock = buildAssetRootCardHeaderBlock();
	assetRowCardRootBlock.appendChild(assetRowRootCardHeaderBlock);

	const image = document.createElement('img');
	image.src = "icons/assets/" + assetCode + "-56x56.png";
	assetRowRootCardHeaderBlock.appendChild(image);

	const assetCodeBlock = document.createElement("span");
	assetCodeBlock.innerText = assetCode;
	assetRowRootCardHeaderBlock.appendChild(assetCodeBlock);

	const assetCardBodyBlock = document.createElement("div");
	assetCardBodyBlock.classList = "card-body";
	assetRowCardRootBlock.appendChild(assetCardBodyBlock);

	const blockChainsRowBlock = document.createElement("div");
	blockChainsRowBlock.classList = "row blockchain-row";
	assetCardBodyBlock.appendChild(blockChainsRowBlock);

	for (var blockchain of blockchains) {
		const blockChainRowBlock = buildBlockchainUIBlock(blockchain, balance);
		blockChainsRowBlock.appendChild(blockChainRowBlock);
	}
	return assetRowRootBlock;
}

function buildBlockchainUIBlock(blockchainInfo) {
	const blockChainColBlock = document.createElement("div");
	blockChainColBlock.classList = "col-6";

	const blockChainCardBgLightBlock = document.createElement("div");
	blockChainCardBgLightBlock.classList = "card bg-light";
	blockChainColBlock.appendChild(blockChainCardBgLightBlock);

	const blockChainCardHeaderBlock = document.createElement("div");
	blockChainCardHeaderBlock.classList = "card-header";
	let blockChainTitle;
	if (blockchainInfo.token) { blockChainTitle = blockchainInfo.blockchain + " (Token)"; }
	else { blockChainTitle = blockchainInfo.blockchain; }
	blockChainCardHeaderBlock.innerText = blockChainTitle;
	blockChainCardBgLightBlock.appendChild(blockChainCardHeaderBlock);

	const blockChainCardBodyBlock = document.createElement("div");
	blockChainCardBodyBlock.classList = "card-body";
	blockChainCardBgLightBlock.appendChild(blockChainCardBodyBlock);

	const blockChainCardBodyRowBlock = document.createElement("div");
	blockChainCardBodyRowBlock.classList = "row";
	blockChainCardBodyBlock.appendChild(blockChainCardBodyRowBlock);

	const blockChainCardBodyCol3Block = document.createElement("div");
	blockChainCardBodyCol3Block.classList = "col-6";
	blockChainCardBodyRowBlock.appendChild(blockChainCardBodyCol3Block);

	const blockChainCardBlock = document.createElement("div");
	blockChainCardBlock.classList = "card";
	blockChainCardBodyCol3Block.appendChild(blockChainCardBlock);

	const blockChainCardBodyBalanceBlock = document.createElement("div");
	blockChainCardBodyBalanceBlock.classList = "card-body";
	blockChainCardBlock.appendChild(blockChainCardBodyBalanceBlock);

	const assetCardTitleBalanceBlock = document.createElement("h5");
	assetCardTitleBalanceBlock.classList = "card-title";
	assetCardTitleBalanceBlock.innerText = "Balance:";
	blockChainCardBodyBalanceBlock.appendChild(assetCardTitleBalanceBlock);

	const assetCardTextBalanceBlock = document.createElement("p");
	assetCardTextBalanceBlock.classList = "card-text";
	let blockChainBalanceTitle;
	if (blockchainInfo.balance !== null) { blockChainBalanceTitle = blockchainInfo.balance; }
	else { blockChainBalanceTitle = "UNKNOWN"; }
	assetCardTextBalanceBlock.innerText = blockChainBalanceTitle;
	blockChainCardBodyBalanceBlock.appendChild(assetCardTextBalanceBlock);

	const blockChainCardBodyCol9Block = document.createElement("div");
	blockChainCardBodyCol9Block.classList = "col-6";
	blockChainCardBodyRowBlock.appendChild(blockChainCardBodyCol9Block);

	const blockChainCol9CardBlock = document.createElement("div");
	blockChainCol9CardBlock.classList = "card";
	blockChainCardBodyCol9Block.appendChild(blockChainCol9CardBlock);

	const blockChainCol9CardBodyBlock = document.createElement("div");
	blockChainCol9CardBodyBlock.classList = "card-body";
	blockChainCol9CardBodyBlock.innerText = "Explorers";
	blockChainCol9CardBlock.appendChild(blockChainCol9CardBodyBlock);

	const assetCardTextExplorersULBlock = document.createElement("ul");
	assetCardTextExplorersULBlock.classList = "card-text";
	blockChainCol9CardBodyBlock.appendChild(assetCardTextExplorersULBlock);

	for (var code in blockchainInfo.alternatives) {
		const assetListExplorersLiBlock = document.createElement("li");
		const el = document.createElement("a");
		el.href = blockchainInfo.alternatives[code];
		el.innerText = code;
		assetListExplorersLiBlock.appendChild(el);
		assetCardTextExplorersULBlock.appendChild(assetListExplorersLiBlock);
	}

	return blockChainColBlock;
}
