class Explorer:
	def __init__(self, name: str) -> None:
		self._name = name

	@property
	def name(self):
		return self._name


BinancemintscanExplorer = Explorer("io.binance.mintscan")

BitinfochartsExplorer = Explorer("com.bitinfocharts")

BitqueryExplorer = Explorer("io.explorer.bitquery")

BlockchainExplorer = Explorer("com.blockchain")

BlockchairExplorer = Explorer("com.blockchair")

BlockcypherExplorer = Explorer("com.blockcypher")

BlockexplorerExplorer = Explorer("one.blockexplorer")

BscscanExplorer = Explorer("com.bscscan")

BtcExplorer = Explorer("com.btc")

ChainzcryptoidExplorer = Explorer("info.chainz.cryptoid")

DashblockExplorer = Explorer("com.dashblockexplorer")

DogeblocksExplorer = Explorer("com.dogeblocks")

DogechainExplorer = Explorer("info.dogechain")

EtherchainExplorer = Explorer("org.etherchain")

EtherscanExplorer = Explorer("io.etherscan")

EthplorerExplorer = Explorer("io.ethplorer")

LitecoinblockExplorer = Explorer("net.litecoinblockexplorer")

PolygonscanExplorer = Explorer("com.polygonscan")

TronscanExplorer = Explorer("org.tronscan")
