from __future__ import annotations
from typing import Optional
import re
import eth_utils
import base58

class UnparsabeBlockchainAddressException(Exception):
	def __init__(self, address: str):
		super().__init__("Unable to parse blockchain address '%s'" % address)
		self._address = address
	
	@property
	def address(self) -> str:
		return self._address

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
	def parse(cls, address: str) -> list[BlockchainAddress]:
		ethereum_address = EthereumBlockchainAddress.try_parse(address)
		if ethereum_address is not None:
			return [ethereum_address]
		
		dogecoin_address = DogecoinBlockchainAddress.try_parse(address)
		if dogecoin_address is not None:
			return [dogecoin_address]

		bitcoin_address = BitcoinBlockchainAddress.try_parse(address)
		if bitcoin_address is not None:
			return [bitcoin_address]
	
		raise UnparsabeBlockchainAddressException(address)

	def __init__(self, data: bytes) -> None:
		self._data = bytes(data)

	@property
	def data(self):
		return self._data

class BitcoinBlockchainAddress(BlockchainAddress):
	"""
	A class represents an Bitcoin Address.

	Supported BIPs:
	- TBD1
	- TBD2

	Static Methods
	-------
	parse(address: str) -> BitcoinBlockchainAddress:
		Parse a string representation of an address to specific `BitcoinBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.

	try_parse(address: str) -> Optional[BitcoinBlockchainAddress]:
		Parse a string representation of an address to specific `BitcoinBlockchainAddress`.
		Returns `None` if address is not parsable.

	Properties
	----------
	data: bytes
		raw representation of address (in bytes)
	"""

	@classmethod
	def parse(cls, address: str) -> BitcoinBlockchainAddress:
		"""
		Parse a string representation of an address to specific `BitcoinBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.
		"""
		blockchain_address: Optional[BitcoinBlockchainAddress] = cls.try_parse(address)
		if blockchain_address is not None:
			return blockchain_address
		raise UnparsabeBlockchainAddressException(address)

	@classmethod
	def try_parse(cls, address: str) -> Optional[BitcoinBlockchainAddress]:
		"""
		Parse a string representation of an address to specific `BitcoinBlockchainAddress`.
		Returns `None` if address is not parsable.
		"""
		raise Exception("Not impelented yet")

	def __init__(self, data: bytes) -> None:
		# if len(data) != ???:
		# 	raise Exception("Wrong data for address")
		super().__init__(data)

class BitcoincashBlockchainAddress(BlockchainAddress):
	"""
	A class represents an BitcoinCash Address.

	Supported BIPs:
	- TBD1
	- TBD2

	Static Methods
	-------
	parse(address: str) -> BitcoincashBlockchainAddress:
		Parse a string representation of an address to specific `BitcoincashBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.

	try_parse(address: str) -> Optional[BitcoincashBlockchainAddress]:
		Parse a string representation of an address to specific `BitcoincashBlockchainAddress`.
		Returns `None` if address is not parsable.

	Properties
	----------
	data: bytes
		raw representation of address (in bytes)

	References
	----------
	- https://bitcoin.stackexchange.com/questions/69056/bitcoin-cash-cash-address-format
	"""

	@classmethod
	def parse(cls, address: str) -> BitcoincashBlockchainAddress:
		"""
		Parse a string representation of an address to specific `BitcoincashBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.
		"""
		blockchain_address: Optional[BitcoincashBlockchainAddress] = cls.try_parse(address)
		if blockchain_address is not None:
			return blockchain_address
		raise UnparsabeBlockchainAddressException(address)

	@classmethod
	def try_parse(cls, address: str) -> Optional[BitcoincashBlockchainAddress]:
		"""
		Parse a string representation of an address to specific `BitcoincashBlockchainAddress`.
		Returns `None` if address is not parsable.
		"""
		raise Exception("Not impelented yet")

	def __init__(self, data: bytes) -> None:
		# if len(data) != ???:
		# 	raise Exception("Wrong data for address")
		super().__init__(data)

class EthereumBlockchainAddress(BlockchainAddress):
	"""
	A class represents an Ethereum Address.

	Supported EIPs:
	- Legacy Ethereum address described in the [Whitepaper](https://ethereum.org/en/whitepaper/)
	- [EIP-55](https://eips.ethereum.org/EIPS/eip-55): Mixed-case checksum address encoding.

	Static Methods
	-------
	parse(address: str) -> EthereumBlockchainAddress:
		Parse a string representation of an address to specific `EthereumBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.

	try_parse(address: str) -> Optional[EthereumBlockchainAddress]:
		Parse a string representation of an address to specific `EthereumBlockchainAddress`.
		Returns `None` if address is not parsable.

	Properties
	----------
	data: bytes
		raw representation of address (in bytes)
	"""

	@classmethod
	def parse(cls, address: str) -> EthereumBlockchainAddress:
		"""
		Parse a string representation of an address to specific `EthereumBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.
		"""
		blockchain_address: Optional[EthereumBlockchainAddress] = cls.try_parse(address)
		if blockchain_address is not None:
			return blockchain_address
		raise UnparsabeBlockchainAddressException(address)

	@classmethod
	def try_parse(cls, address: str) -> Optional[EthereumBlockchainAddress]:
		"""
		Parse a string representation of an address to specific `EthereumBlockchainAddress`.
		Returns `None` if address is not parsable.
		"""
		if cls._validation_regex_legacy.match(address):
			address_data_str: str = address[2:]
			address_data: bytes = bytes.fromhex(address_data_str)
			blockchain_address: EthereumBlockchainAddress = EthereumBlockchainAddress(address_data)
			return blockchain_address
		else:
			# TODO validate address by EIP-55 https://eips.ethereum.org/EIPS/eip-55
			raise Exception("Not impelented yet")

	_validation_regex_legacy = re.compile(r"^0x[0-9a-f]{40}$")
	_validation_regex_eip55 = re.compile(r"^0x[0-9a-fA-F]{40}$")

	def __init__(self, data: bytes) -> None:
		super().__init__(data)

	def as_legacy_address(self) -> str:
		address_data_str: str = self._data.hex()
		return "0x%s" % address_data_str

	def as_eip55_address(self) -> str:
		# See https://eips.ethereum.org/EIPS/eip-55
		
		hex_address = self._data.hex()
		checksummed_buffer = ""
		hashed_address = eth_utils.keccak(text=hex_address).hex()
		for nibble_index, character in enumerate(hex_address):
			if character in "0123456789":
				checksummed_buffer += character
			elif character in "abcdef" or "ABCDEF":
				hashed_address_nibble = int(hashed_address[nibble_index], 16)

				if hashed_address_nibble > 7:
					checksummed_buffer += character.upper()
				else:
					checksummed_buffer += character
			else:
				raise eth_utils.ValidationError(
						f"Unrecognized hex character {character!r} at position {nibble_index}"
						)
		address_data_str = "0x%s" % checksummed_buffer
		return address_data_str 

#
# To future implementation
#
# class Eip3770BlockchainAddress(EthereumBlockchainAddress):
# 	"""
# 	A class represents EIP-3770: Chain-specific addresses.
# 	See https://eips.ethereum.org/EIPS/eip-3770
# 	"""
#
# 	def __init__(self, data: bytes) -> None:
# 		super().__init__(data)

class DogecoinBlockchainAddress(BlockchainAddress):

	@classmethod
	def parse(cls, address: str) -> DogecoinBlockchainAddress:
		"""
		Parse a string representation of an address to specific `DogecoinBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.
		"""
		blockchain_address: Optional[DogecoinBlockchainAddress] = cls.try_parse(address)
		if blockchain_address is not None:
			return blockchain_address
		raise UnparsabeBlockchainAddressException(address)

	@classmethod
	def try_parse(cls, address: str) -> Optional[DogecoinBlockchainAddress]:
		
		"""
		Parse a string representation of an address to specific `DogecoinBlockchainAddress`.
		Returns `None` if address is not parsable.
		"""
		_validation_regex_Dogecoin= re.compile(r"^D[0-9a-zA-Z]{25-34}$")
		if _validation_regex_Dogecoin.match(address):
			address_data: bytes = base58.b58encode(address)

			blockchain_address: DogecoinBlockchainAddress = DogecoinBlockchainAddress(address_data)
			return blockchain_address
		else:
			raise Exception("Wrong address data")

	def __init__(self, data: bytes) -> None:
		super().__init__(data)

	def as_legacy_address_dogecoin(self) -> str:
		address_data_decode: bytes = base58.b58decode(self._data)
		address_data_str: str = str(address_data_decode, 'UTF-8')
		return address_data_str
