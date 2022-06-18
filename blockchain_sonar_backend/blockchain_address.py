from __future__ import annotations
from audioop import add

import re

class BlockchainAddress(object):
	"""
	A base class to represent an Blockchain Address.

	Static Methods
	-------
	parse(address: str):
		Parse a string representation of an address to specific `BlockchainAddress`

	Properties
	----------
	data: bytes
		raw representation of address (in bytes)
	"""

	@classmethod
	def parse(cls, address: str) -> BlockchainAddress:
		if BlockchainAddress._isBitcoin(address):
			return BitcoinBlockchainAddress.parse(address)
		elif BlockchainAddress._isEip55(address):
			return Eip55BlockchainAddress.parse(address)
		else:
			raise Exception("Unsupported address: %s" % address)

	def __init__(self, data: bytes) -> None:
		self._data = bytes(data)

	@property
	def data(self):
		return self._data

	@staticmethod
	def _isBitcoin(address: str) -> bool:
		# TODO
		return False

	@staticmethod
	def _isEip55(address: str) -> bool:
		if Eip55BlockchainAddress.get_validation_regex().match(address):
			return True
		return False

class BitcoinBlockchainAddress(BlockchainAddress):
	"""
	A class to represent an Bitcoin (Legacy) Address.
	See ???

	Static Methods
	-------
	parse(address: str) -> BitcoinBlockchainAddress:
		Parse a string representation of an address to specific `BitcoinBlockchainAddress`

	Properties
	----------
	data: bytes
		raw representation of address (in bytes)
	"""

	@staticmethod
	def parse(address: str) -> BitcoinBlockchainAddress:
		raise Exception("Not implelented yet")

	def __init__(self, data: bytes) -> None:
		# if len(data) != ???:
		# 	raise Exception("Wrong data for address")
		super().__init__(data)

class Eip55BlockchainAddress(BlockchainAddress):
	"""
	A class represents EIP-55: Mixed-case checksum address encoding.
	See https://eips.ethereum.org/EIPS/eip-55

	Static Methods
	-------
	parse(address: str) -> Eip55BlockchainAddress:
		Parse a string representation of an address to specific `Eip55BlockchainAddress`

	Properties
	----------
	data: bytes
		raw representation of address (in bytes)
	"""

	@classmethod
	def parse(cls, blockchain_address: str) -> Eip55BlockchainAddress:
		if cls._validation_regex_legacy.match(blockchain_address):
			pass
		else:
			# TODO validate address by EIP-55 https://eips.ethereum.org/EIPS/eip-55
			pass

		address_data_str: str = blockchain_address[2:]
		address_data: bytes = bytes.fromhex(address_data_str)
		blockchain_address: Eip55BlockchainAddress = Eip55BlockchainAddress(address_data)
		return blockchain_address

	@classmethod
	def get_validation_regex(cls) -> re.Pattern:
		return cls._validation_regex

	_validation_regex_legacy = re.compile(r"^0x[0-9a-f]{40}$")
	_validation_regex = re.compile(r"^0x[0-9a-fA-F]{40}$")

	def __init__(self, data: bytes) -> None:
		super().__init__(data)

	def to_legacy_address(self) -> str:
		address_data_str: str = self._data.hex()
		return "0x%s" % address_data_str

	def to_eip55_address(self) -> str:
		# See https://eips.ethereum.org/EIPS/eip-55
		raise Exception("Not implemented")

#
# To future implementation
#
# class Eip3770BlockchainAddress(Eip55BlockchainAddress):
# 	"""
# 	A class represents EIP-3770: Chain-specific addresses.
# 	See https://eips.ethereum.org/EIPS/eip-3770

# 	Static Methods
# 	-------
# 	parse(address: str) -> Eip55BlockchainAddress:
# 		Parse a string representation of an address to specific `Eip55BlockchainAddress`

# 	Properties
# 	----------
# 	data: bytes
# 		raw representation of address (in bytes)
# 	"""

# 	@classmethod
# 	def parse(address: str) -> Eip55BlockchainAddress:
# 		raise Exception("Not implemented yet")

# 	def __init__(self, data: bytes) -> None:
# 		super().__init__(data)
