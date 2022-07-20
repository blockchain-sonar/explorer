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


BTC = Asset("BTC", "Bitcoin", [
	AssetRepresentationBlockchain(BitcoinBlockchain, False, [
		AssetRepresentationExplorer(BlockchairExplorer, "https://blockchair.com/bitcoin/address/%s"),
		AssetRepresentationExplorer(BlockcypherExplorer, ""),
		AssetRepresentationExplorer(BtcExplorer, ""),
		AssetRepresentationExplorer(BitinfochartsExplorer, ""),
		AssetRepresentationExplorer(TokenviewExplorer, ""),
		AssetRepresentationExplorer(BitqueryExplorer, ""),
		AssetRepresentationExplorer(BlockexplorerExplorer, "https://blockexplorer.one/bitcoin/mainnet/address/%s")
	])
])

ETH = Asset("ETH", "Ether", [
	AssetRepresentationBlockchain(EthereumBlockchain, False, [
		AssetRepresentationExplorer(EtherscanExplorer, "https://etherscan.io/address/%s"),
		AssetRepresentationExplorer(EthplorerExplorer, "https://ethplorer.io/address/%s"),
		AssetRepresentationExplorer(EtherchainExplorer, "https://etherchain.org/account/%s"),
	])
])

MATIC = Asset("MATIC", "Polygon", [
	AssetRepresentationBlockchain(EthereumBlockchain, True),
	AssetRepresentationBlockchain(PolygonBlockchain, False)
])

USDT = Asset("USDT", "Tether",[
	AssetRepresentationBlockchain(EthereumBlockchain, True, [
		AssetTokenRepresentationExplorer(EtherscanExplorer, "https://etherscan.io/address/%s", "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7?a=%s"),
		AssetRepresentationExplorer(EthplorerExplorer, "https://ethplorer.io/address/%s"),
		AssetRepresentationExplorer(EtherchainExplorer, "https://etherchain.org/account/%s"),
	]),
	AssetRepresentationBlockchain(TronBlockchain, True, [
		AssetRepresentationExplorer(TronscanExplorer, "https://tronscan.org/#/address/%s/"),
	])
])
