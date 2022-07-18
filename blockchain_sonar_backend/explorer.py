class Explorer:
	def __init__(self, name: list[str]) -> None:
		self._name = name

	@property
	def name(self):
		return self._name

from blockchain_sonar_backend.explorer import ExplorerV1Controller
explorer = ExplorerV1Controller()
address_str = explorer.address_str
EthereumExplorer = Explorer(["com.blockchair: https://blockchair.com/ethereum/address/%s" %address_str,
							"com.blockcypher: https://live.blockcypher.com/eth/address/%s/" %address_str,
							"io.etherscan: https://etherscan.io/address/%s" %address_str,
							"io.ethplorer: https://ethplorer.io/address/%s" %address_str,
							"org.etherchain: https://etherchain.org/account/%s" %address_str
							])

USDTExplorer = Explorer(["io.etherscan: https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7?a=%s" %address_str])

BNBExplorer = Explorer(["com.bscscan: https://bscscan.com/address/%s" %address_str])

BUSDTExplorer = Explorer(["com.bscscan: https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955?a=%s" %address_str])

MATICExplorer = Explorer(["com.polygonscan: https://polygonscan.com/address/%s" %address_str])
