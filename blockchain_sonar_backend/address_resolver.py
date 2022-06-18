from blockchain_sonar_backend.blockchain_address import BitcoinBlockchainAddress, BlockchainAddress, Eip55BlockchainAddress


def address_resolve(address: BlockchainAddress) -> list[str]:
	if isinstance(address, BitcoinBlockchainAddress):
		return ["bitcoin"]
	elif isinstance(address, Eip55BlockchainAddress):
		return ["ethereum", "polygon", "bsc"]
	else:
		raise Exception("Not supported address")
