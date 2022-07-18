from __future__ import annotations

from blockchain_sonar_backend.blockchain import BitcoinBlockchain, Blockchain, EthereumBlockchain, PolygonBlockchain, TronBlockchain

class Asset:
	def __init__(self, code, name, blockchain_representations: list[AssetRepresentation]) -> None:
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
	def blockchain_representation(self) -> list[AssetRepresentation]:
		return self._blockchain_representations

class AssetRepresentation:
	def __init__(self, blockchain: Blockchain, is_token: bool) -> None:
		self._blockchain = blockchain
		self._is_token = is_token

	@property
	def blockchain(self) -> Blockchain:
		return self._blockchain

	@property
	def is_token(self) -> bool:
		return self._is_token

BTC = Asset("BTC", "Bitcoin", [
	AssetRepresentation(BitcoinBlockchain, False)
])

ETH = Asset("ETH", "Ether", [
	AssetRepresentation(EthereumBlockchain, False)
])

MATIC = Asset("MATIC", "Polygon", [
	AssetRepresentation(EthereumBlockchain, True),
	AssetRepresentation(PolygonBlockchain, False)
])

USDT = Asset("USDT", "Tether",[
	AssetRepresentation(EthereumBlockchain, True),
	AssetRepresentation(TronBlockchain, True)
])
