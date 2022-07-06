from blockchain_sonar_backend.blockchain_address import BitcoinBlockchainAddress, BlockchainAddress, EthereumBlockchainAddress,DogecoinBlockchainAddress, LitecoinBlockchainAddress, TronBlockchainAddress, DashBlockchainAddress


def blockchain_resolve(address: BlockchainAddress) -> list[str]:
	if isinstance(address, BitcoinBlockchainAddress):
		return ["bitcoin"]
	elif isinstance(address, EthereumBlockchainAddress):
		return ["ethereum", "polygon", "bsc"]
	elif isinstance(address, DogecoinBlockchainAddress):
		return ["dogecoin"]
	elif isinstance(address, LitecoinBlockchainAddress):
		return ["litecoin"]
	elif isinstance(address, TronBlockchainAddress):
		return ["tron"]
	elif isinstance(address, DashBlockchainAddress):
		return ["dash"]

	else:
		raise Exception("Not supported address")
