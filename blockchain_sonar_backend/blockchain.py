class Blockchain:
	def __init__(self, name: str) -> None:
		self._name = name

	@property
	def name(self):
		return self._name


BitcoinBlockchain = Blockchain("Bitcoin")

EthereumBlockchain = Blockchain("Ethereum")

DogecoinBlockchain = Blockchain("Dogecoin")

LitecoinBlockchain = Blockchain("Litecoin")

PolygonBlockchain = Blockchain("Polygon")

TronBlockchain = Blockchain("Tron")
