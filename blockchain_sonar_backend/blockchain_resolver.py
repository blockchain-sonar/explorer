from blockchain_sonar_backend.blockchain_address import BitcoinBlockchainAddress, BlockchainAddress, EthereumBlockchainAddress


def blockchain_resolve(address: BlockchainAddress) -> list[str]:
	if isinstance(address, BitcoinBlockchainAddress):
		return ["bitcoin"]
	elif isinstance(address, EthereumBlockchainAddress):
		return ["ethereum", "polygon", "bsc"]
	else:
		raise Exception("Not supported address")
