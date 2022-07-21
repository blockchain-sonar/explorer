class Blockchain:
	def __init__(self, name: str) -> None:
		self._name = name

	@property
	def name(self):
		return self._name


BitcoinBlockchain = Blockchain("Bitcoin")

DashBlockchain = Blockchain("Dash")

DogecoinBlockchain = Blockchain("Dogecoin")

EthereumBlockchain = Blockchain("Ethereum")

LitecoinBlockchain = Blockchain("Litecoin")

PolygonBlockchain = Blockchain("Polygon")

TronBlockchain = Blockchain("Tron")
