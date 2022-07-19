class Explorer:
	def __init__(self, name: str) -> None:
		self._name = name

	@property
	def name(self):
		return self._name


EtherscanExplorer = Explorer("io.etherscan")

BlockchairExplorer = Explorer("com.blockchair")

BlockcypherExplorer = Explorer("com.blockcypher")

EthplorerExplorer = Explorer("io.ethplorer")

EtherchainExplorer = Explorer("org.etherchain")

BscscanExplorer = Explorer("com.bscscan")

PolygonscanExplorer = Explorer("com.polygonscan")

BlockchainExplorer = Explorer("com.blockchain")

LitecoinblockExplorer = Explorer("net.litecoinblockexplorer")

BtcExplorer = Explorer("com.btc")

BitinfochartsExplorer = Explorer("com.bitinfocharts")

DogechainExplorer = Explorer("info.dogechain")

DogeblocksExplorer = Explorer("com.dogeblocks")

TokenviewExplorer = Explorer("com.tokenview")

ExplorerBitqueryExplorer = Explorer("io.explorer.bitquery")

BlockexplorerExplorer = Explorer("one.blockexplorer")
