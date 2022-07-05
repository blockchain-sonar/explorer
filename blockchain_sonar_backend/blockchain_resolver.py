from blockchain_sonar_backend.blockchain_address import BitcoinBlockchainAddress, BlockchainAddress, EthereumBlockchainAddress,DogecoinBlockchainAddress, LitecoinBlockchainAddress


def blockchain_resolve(address: BlockchainAddress) -> list[str]:
	if isinstance(address, BitcoinBlockchainAddress):
		return ["bitcoin"]
	elif isinstance(address, EthereumBlockchainAddress):
		return ["ethereum", "polygon", "bsc"]
	elif isinstance(address, DogecoinBlockchainAddress):
		return ["dogecoin"]
	elif isinstance(address, LitecoinBlockchainAddress):
		return ["litecoin"]

	else:
		raise Exception("Not supported address")
