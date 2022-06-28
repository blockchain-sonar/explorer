from blockchain_sonar_backend.blockchain_address import BitcoinBlockchainAddress, BlockchainAddress, EthereumBlockchainAddress,DogecoinBlockchainAddress


def blockchain_resolve(address: BlockchainAddress) -> list[str]:
	if isinstance(address, BitcoinBlockchainAddress):
		return ["bitcoin"]
	elif isinstance(address, EthereumBlockchainAddress):
		return ["ethereum", "polygon", "bsc"]
	elif isinstance(address, DogecoinBlockchainAddress):
		return ["dogecoin"]

	else:
		raise Exception("Not supported address")
