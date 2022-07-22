from __future__ import annotations

from blockchain_sonar_backend.blockchain import *
from blockchain_sonar_backend.explorer import *

class Asset:
	def __init__(self, code, name, blockchain_representations: list[AssetRepresentationBlockchain]) -> None:
		self._code = code
		self._name = name
		self._blockchain_representations = blockchain_representations

	@property
	def code(self) -> str:
		return self._code

	@property
	def name(self) -> str:
		return self._name

	@property
	def blockchain_representation(self) -> list[AssetRepresentationBlockchain]:
		return self._blockchain_representations

class AssetRepresentationBlockchain:
	def __init__(self, blockchain: Blockchain, is_token: bool, representation_explorers: list[AssetRepresentationExplorer]) -> None:
		self._blockchain = blockchain
		self._is_token = is_token
		self._representation_explorers = representation_explorers

	@property
	def blockchain(self) -> Blockchain:
		return self._blockchain

	@property
	def is_token(self) -> bool:
		return self._is_token

	@property
	def representation_explorers(self) -> list[AssetRepresentationExplorer]:
		return self._representation_explorers

class AssetRepresentationExplorer:
	def __init__(self, explorer: Explorer, address_url_template: str) -> None:
		self._explorer = explorer
		self._address_url_template = address_url_template

	@property
	def explorer(self) -> Explorer:
		return self._explorer

	@property
	def address_url_template(self) -> str:
		return self._address_url_template

class AssetTokenRepresentationExplorer(AssetRepresentationExplorer):
	def __init__(self, explorer: Explorer, address_url_template: str, token_url_template: str) -> None:
		super().__init__(explorer, address_url_template)
		self._token_url_template = token_url_template

	@property
	def token_url_template(self) -> str:
		return self._token_url_template


BNB = Asset("BNB", "Binance Coin", [
	AssetRepresentationBlockchain(BinanceSmartChainBlockchain, False, [
		AssetRepresentationExplorer(BinancemintscanExplorer, "https://binance.mintscan.io/account/%s"),
		AssetRepresentationExplorer(BitqueryExplorer, "https://explorer.bitquery.io/bsc/address/%s"),
		AssetRepresentationExplorer(BscscanExplorer, "https://bscscan.com/address/%s"),
	]),
	AssetRepresentationBlockchain(EthereumBlockchain, True, [
		AssetTokenRepresentationExplorer(EtherscanExplorer, "https://etherscan.io/address/%s", "https://etherscan.io/token/0xB8c77482e45F1F44dE1745F52C74426C631bDD52?a=%s"),
	])
])

BTC = Asset("BTC", "Bitcoin", [
	AssetRepresentationBlockchain(BitcoinBlockchain, False, [
		AssetRepresentationExplorer(BitinfochartsExplorer, "https://bitinfocharts.com/bitcoin/address/%s"),
		AssetRepresentationExplorer(BitqueryExplorer, "https://explorer.bitquery.io/bitcoin/address/%s"),
		AssetRepresentationExplorer(BlockchairExplorer, "https://blockchair.com/bitcoin/address/%s"),
		AssetRepresentationExplorer(BlockcypherExplorer, "https://live.blockcypher.com/btc/address/%s/"),
		AssetRepresentationExplorer(BlockexplorerExplorer, "https://blockexplorer.one/bitcoin/mainnet/address/%s"),
		AssetRepresentationExplorer(BtcExplorer, "https://explorer.btc.com/btc/address/%s"),
	])
])

BUSDT = Asset("BUSD-T", "BUSD Token", [
	AssetRepresentationBlockchain(EthereumBlockchain, True, [
		AssetRepresentationExplorer(BitqueryExplorer, "https://explorer.bitquery.io/bsc/token/%s"),
		AssetRepresentationExplorer(BscscanExplorer, "https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955?a=%s")
	])
])

Dash = Asset("DASH", "Dash", [
	AssetRepresentationBlockchain(DashBlockchain, False, [
		AssetRepresentationExplorer(BitinfochartsExplorer, "https://bitinfocharts.com/dash/address/%s"),
		AssetRepresentationExplorer(BitqueryExplorer, "https://explorer.bitquery.io/dash/address/%s"),
		AssetRepresentationExplorer(BlockchairExplorer, "https://blockchair.com/dash/address/%s"),
		AssetRepresentationExplorer(BlockcypherExplorer, "https://live.blockcypher.com/dash/address/%s/"),
		AssetRepresentationExplorer(ChainzcryptoidExplorer, "https://chainz.cryptoid.info/dash/address.dws?%s.htm"),
		AssetRepresentationExplorer(DashblockExplorer, "https://dashblockexplorer.com/address/%s"),
	])
])

Dogecoin = Asset("DOGE", "Dogecoin", [
	AssetRepresentationBlockchain(DogecoinBlockchain, False, [
		AssetRepresentationExplorer(BitinfochartsExplorer,"https://bitinfocharts.com/dogecoin/address/%s"),
		AssetRepresentationExplorer(BlockchairExplorer, "https://blockchair.com/dogecoin/address/%s"),
		AssetRepresentationExplorer(BlockcypherExplorer, "https://live.blockcypher.com/doge/address/%s/"),
		AssetRepresentationExplorer(DogeblocksExplorer, "https://dogeblocks.com/address/%s"),
		AssetRepresentationExplorer(DogechainExplorer, "https://dogechain.info/address/%s")
	])
])

ETH = Asset("ETH", "Ether", [
	AssetRepresentationBlockchain(EthereumBlockchain, False, [
		AssetRepresentationExplorer(EtherchainExplorer, "https://etherchain.org/account/%s"),
		AssetRepresentationExplorer(EtherscanExplorer, "https://etherscan.io/address/%s"),
		AssetRepresentationExplorer(EthplorerExplorer, "https://ethplorer.io/address/%s")
	]),
	AssetRepresentationBlockchain(BinanceSmartChainBlockchain, True, [
		AssetTokenRepresentationExplorer(BscscanExplorer, "https://bscscan.com/address/%s", "https://bscscan.com/token/0x2170ed0880ac9a755fd29b2688956bd959f933f8?a=%s"),
	])
])

Litecoin = Asset("LTC", "Litecoin", [
	AssetRepresentationBlockchain(LitecoinBlockchain, False, [
		AssetRepresentationExplorer(BitinfochartsExplorer, "https://bitinfocharts.com/ru/litecoin/address/%s"),
		AssetRepresentationExplorer(BlockcypherExplorer, "https://live.blockcypher.com/ltc/address/%s/"),
		AssetRepresentationExplorer(BlockexplorerExplorer, "https://blockexplorer.one/litecoin/mainnet/address/%s"),
		AssetRepresentationExplorer(BtcExplorer, "https://explorer.btc.com/ltc/%s"),
		AssetRepresentationExplorer(ChainzcryptoidExplorer, "https://chainz.cryptoid.info/ltc/address.dws?%s.htm"),
		AssetRepresentationExplorer(LitecoinblockExplorer, "https://litecoinblockexplorer.net/address/%s")
	])
])

MATIC = Asset("MATIC", "Polygon", [
	AssetRepresentationBlockchain(EthereumBlockchain, True, [
		AssetRepresentationExplorer(BlockchainExplorer,  "https://blockchair.com/ethereum/erc-20/token/%s"),
		AssetRepresentationExplorer(BitqueryExplorer, "https://explorer.bitquery.io/matic/address/%s")
	]),
	AssetRepresentationBlockchain(PolygonBlockchain, False, [
		AssetRepresentationExplorer(PolygonscanExplorer, "https://polygonscan.com/address/%s")
	])
])

Tron = Asset("TRX", "Tron", [
	AssetRepresentationBlockchain(TronBlockchain, False, [
		AssetRepresentationExplorer(BitqueryExplorer, "https://explorer.bitquery.io/tron/address/%s"),
		AssetRepresentationExplorer(TronscanExplorer, "https://tronscan.org/#/address/%s/")
	])
])

USDT = Asset("USDT", "Tether",[
	AssetRepresentationBlockchain(EthereumBlockchain, True, [
		AssetTokenRepresentationExplorer(EtherscanExplorer, "https://etherscan.io/address/%s", "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7?a=%s"),
		AssetRepresentationExplorer(EtherchainExplorer, "https://etherchain.org/account/%s"),
		AssetRepresentationExplorer(EthplorerExplorer, "https://ethplorer.io/address/%s"),
	]),
	AssetRepresentationBlockchain(TronBlockchain, True, [
		AssetRepresentationExplorer(TronscanExplorer, "https://tronscan.org/#/address/%s/")
	])
])
