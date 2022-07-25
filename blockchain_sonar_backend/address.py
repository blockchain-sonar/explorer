from __future__ import annotations
from typing import Optional
import re
import eth_utils
import base58

class UnparsableAddressException(Exception):
	def __init__(self, address: str):
		super().__init__("Unable to parse blockchain address '%s'" % address)
		self._address = address
	
	@property
	def address(self) -> str:
		return self._address

class AddressVisitor(object):
	def visitBitcoinBlockchainAddress(self, address: BitcoinBlockchainAddress):
		raise Exception("Abstart method")

	def visitBitcoincashBlockchainAddress(self, address: BitcoincashBlockchainAddress):
		raise Exception("Abstart method")

	def visitDashBlockchainAddress(self, address: DashBlockchainAddress):
		raise Exception("Abstart method")

	def visitDogecoinBlockchainAddress(self, address: DogecoinBlockchainAddress):
		raise Exception("Abstart method")

	def visitEthereumBlockchainAddress(self, address: EthereumBlockchainAddress):
		raise Exception("Abstart method")

	def visitLitecoinBlockchainAddress(self, address: LitecoinBlockchainAddress):
		raise Exception("Abstart method")

	def visitTronBlockchainAddress(self, address: TronBlockchainAddress):
		raise Exception("Abstart method")

class Address(object):
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
	def parse(cls, address: str) -> list[Address]:
		ethereum_address = EthereumBlockchainAddress.try_parse(address)
		if ethereum_address is not None:
			return [ethereum_address]

		dogecoin_address = DogecoinBlockchainAddress.try_parse(address)
		if dogecoin_address is not None:
			return [dogecoin_address]
		
		litecoin_address = LitecoinBlockchainAddress.try_parse(address)
		if litecoin_address is not None:
			return [litecoin_address]

		tron_address = TronBlockchainAddress.try_parse(address)
		if tron_address is not None:
			return [tron_address]

		dash_address = DashBlockchainAddress.try_parse(address)
		if dash_address is not None:
			return [dash_address]

		bitcoin_address = BitcoinBlockchainAddress.try_parse(address)
		if bitcoin_address is not None:
			return [bitcoin_address]
		
		raise UnparsableAddressException(address)

	def __init__(self, data: bytes) -> None:
		self._data = bytes(data)

	@property
	def data(self):
		return self._data

	def accept(self, visitor: AddressVisitor):
		raise Exception("Abstart method")

	def as_string(self) -> str:
		raise Exception("Abstart method")

class BitcoinBlockchainAddress(Address):
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

	References
	----------
	https://en.bitcoin.it/wiki/List_of_address_prefixes
	https://en.bitcoin.it/wiki/Bech32
	https://coin.space/all-about-address-types/
	http://lenschulwitz.com/base58
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
		raise UnparsableAddressException(address)

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

	def accept(self, visitor: AddressVisitor):
		visitor.visitBitcoinBlockchainAddress(self)

	def as_string(self) -> str:
		raise Exception("Not impelented yet")

class BitcoincashBlockchainAddress(Address):
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
		raise UnparsableAddressException(address)

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

	def accept(self, visitor: AddressVisitor):
		visitor.visitBitcoincashBlockchainAddress(self)

	def as_string(self) -> str:
		raise Exception("Not impelented yet")

class EthereumBlockchainAddress(Address):
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
		raise UnparsableAddressException(address)

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
		if cls._validation_regex_eip55.match(address):
			address_data_str: str = address[2:]
			address_data: bytes = bytes.fromhex(address_data_str)
			blockchain_address: EthereumBlockchainAddress = EthereumBlockchainAddress(address_data)
			return blockchain_address
		else:
			return None

	_validation_regex_legacy = re.compile(r"^0x[0-9a-f]{40}$")
	_validation_regex_eip55 = re.compile(r"^0x[0-9a-fA-F]{40}$")

	def __init__(self, data: bytes) -> None:
		super().__init__(data)

	def accept(self, visitor: AddressVisitor):
		visitor.visitEthereumBlockchainAddress(self)

	def as_string(self) -> str:
		return self.as_eip55_address()

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
#class Eip3770BlockchainAddress(EthereumBlockchainAddress):
#	"""
#	A class represents EIP-3770: Chain-specific addresses.
#	See https://eips.ethereum.org/EIPS/eip-3770
#	"""
#	def __init__(self, data: bytes) -> None:
#		super().__init__(data)

class DogecoinBlockchainAddress(Address):
	"""
	A class represents an Dogecoin Address.

	Static Methods
	-------
	parse(address: str) -> DogecoinBlockchainAddress:
		Parse a string representation of an address to specific `DogecoinBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.

	try_parse(address: str) -> Optional[DogecoinBlockchainAddress]:
		Parse a string representation of an address to specific `DogecoinBlockchainAddress`.
		Returns `None` if address is not parsable.

	Properties
	----------
	data: bytes
		raw representation of address (in bytes)
	
	References
	----------
	https://support.ledger.com/hc/ru/articles/115005174025-Dogecoin-DOGE-?docs=true
	
	"""

	@classmethod
	def parse(cls, address: str) -> DogecoinBlockchainAddress:
		"""
		Parse a string representation of an address to specific `DogecoinBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.
		"""
		blockchain_address: Optional[DogecoinBlockchainAddress] = cls.try_parse(address)
		if blockchain_address is not None:
			return blockchain_address
		else:
			raise UnparsableAddressException(address)

	@classmethod
	def try_parse(cls, address: str) -> Optional[DogecoinBlockchainAddress]:
		
		"""
		Parse a string representation of an address to specific `DogecoinBlockchainAddress`.
		Returns `None` if address is not parsable.
		"""
		
		if cls._validation_regex_dogecoin.match(address):
			address_data_decode: bytes = base58.b58decode(address)
			blockchain_address: DogecoinBlockchainAddress = DogecoinBlockchainAddress(address_data_decode)
			return blockchain_address
		else:
			return None

	_validation_regex_dogecoin= re.compile(r"^D[0-9a-zA-Z]{26,33}$")

	def __init__(self, data: bytes) -> None:
		super().__init__(data)

	def accept(self, visitor: AddressVisitor):
		visitor.visitDogecoinBlockchainAddress(self)

	def as_string(self) -> str:
		address_data_encode: bytes = base58.b58encode(self._data)
		address_data_str: str = str(address_data_encode, 'UTF-8')
		return address_data_str

class LitecoinBlockchainAddress(Address):
	"""
	A class represents an Dogecoin Address.

	Static Methods
	-------
	parse(address: str) -> LitecoinBlockchainAddress:
		Parse a string representation of an address to specific `LitecoinBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.

	try_parse(address: str) -> Optional[LitecoinBlockchainAddress]:
		Parse a string representation of an address to specific `LitecoinBlockchainAddress`.
		Returns `None` if address is not parsable.

	Properties
	----------
	data: bytes
		raw representation of address (in bytes)
	
	References
	----------
	https://coin.space/all-about-address-types/
	https://bitcoin.stackexchange.com/questions/62781/litecoin-constants-and-prefixes
	https://en.bitcoin.it/wiki/Bech32	
	"""

	@classmethod
	def parse(cls, address: str) -> LitecoinBlockchainAddress:
		"""
		Parse a string representation of an address to specific `LitecoinBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.
		"""
		blockchain_address: Optional[LitecoinBlockchainAddress] = cls.try_parse(address)
		if blockchain_address is not None:
			return blockchain_address
		else:
			raise UnparsableAddressException(address)

	@classmethod
	def try_parse(cls, address: str) -> Optional[LitecoinBlockchainAddress]:
		
		"""
		Parse a string representation of an address to specific `LitecoinBlockchainAddress`.
		Returns `None` if address is not parsable.
		"""
		
		if cls._validation_regex_litecoin.match(address):
			address_data_decode: bytes = base58.b58decode(address)
			blockchain_address: LitecoinBlockchainAddress = LitecoinBlockchainAddress(address_data_decode)
			return blockchain_address
		
		# TODO if cls._validation_regex_Litecoin_ltc1.match(address):
		#			address_ltc1_data_decode: bytes = 
		#			blockchain_address: LitecoinBlockchainAddress = LitecoinBlockchainAddress(address_ltc1_data_decode)
		#			return blockchain_address
		else:
			return None

	_validation_regex_litecoin = re.compile(r"^[LM][0-9a-zA-Z]{33}$")
	# TODO _validation_regex_Litecoin_ltc1 = re.compile(r"^ltc1[0-9a-z]{39,59}$")
	

	def __init__(self, data: bytes) -> None:
		super().__init__(data)

	def accept(self, visitor: AddressVisitor):
		visitor.visitLitecoinBlockchainAddress(self)

	def as_string(self) -> str:
		address_data_encode: bytes = base58.b58encode(self._data)
		address_data_str: str = str(address_data_encode, 'UTF-8')
		return address_data_str

class TronBlockchainAddress(Address):
	"""
	A class represents an Tron Address.

	Static Methods
	-------
	parse(address: str) -> TronBlockchainAddress:
		Parse a string representation of an address to specific `TronBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.

	try_parse(address: str) -> Optional[TronBlockchainAddress]:
		Parse a string representation of an address to specific `TronBlockchainAddress`.
		Returns `None` if address is not parsable.

	Properties
	----------
	data: bytes
		raw representation of address (in bytes)
	
	References
	----------
	https://developers.tron.network/docs/account
	"""

	@classmethod
	def parse(cls, address: str) -> TronBlockchainAddress:
		"""
		Parse a string representation of an address to specific `TRONBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.
		"""
		blockchain_address: Optional[TronBlockchainAddress] = cls.try_parse(address)
		if blockchain_address is not None:
			return blockchain_address
		else:
			raise UnparsableAddressException(address)

	@classmethod
	def try_parse(cls, address: str) -> Optional[TronBlockchainAddress]:
		
		"""
		Parse a string representation of an address to specific `TronBlockchainAddress`.
		Returns `None` if address is not parsable.
		"""
		
		if cls._validation_regex_tron.match(address):
			address_data_decode: bytes = base58.b58decode(address)
			blockchain_address: TronBlockchainAddress = TronBlockchainAddress(address_data_decode)
			return blockchain_address
		else:
			return None

	_validation_regex_tron = re.compile(r"^T[0-9a-zA-Z]{33}$")

	def __init__(self, data: bytes) -> None:
		super().__init__(data)

	def accept(self, visitor: AddressVisitor):
		visitor.visitTronBlockchainAddress(self)

	def as_string(self) -> str:
		address_data_encode: bytes = base58.b58encode(self._data)
		address_data_str: str = str(address_data_encode, 'UTF-8')
		return address_data_str

class DashBlockchainAddress(Address):
	"""
	A class represents an Dash Address.

	Static Methods
	-------
	parse(address: str) -> DashBlockchainAddress:
		Parse a string representation of an address to specific `DashBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.

	try_parse(address: str) -> Optional[DashBlockchainAddress]:
		Parse a string representation of an address to specific `DashBlockchainAddress`.
		Returns `None` if address is not parsable.

	Properties
	----------
	data: bytes
		raw representation of address (in bytes)
	
	References
	----------
	https://bitcoin.stackexchange.com/questions/83507/dash-constants-and-prefixes
	"""

	@classmethod
	def parse(cls, address: str) -> DashBlockchainAddress:
		"""
		Parse a string representation of an address to specific ` DashBlockchainAddress`
		Raise `UnparsabeBlockchainAddressException` if address is not parsable.
		"""
		blockchain_address: Optional[DashBlockchainAddress] = cls.try_parse(address)
		if blockchain_address is not None:
			return blockchain_address
		else:
			raise UnparsableAddressException(address)

	@classmethod
	def try_parse(cls, address: str) -> Optional[DashBlockchainAddress]:
		
		"""
		Parse a string representation of an address to specific `DashBlockchainAddress`.
		Returns `None` if address is not parsable.
		"""
		
		if cls._validation_regex_dash.match(address):
			address_data_decode: bytes = base58.b58decode(address)
			blockchain_address: DashBlockchainAddress = DashBlockchainAddress(address_data_decode)
			return blockchain_address
		else:
			return None

	_validation_regex_dash= re.compile(r"^X[0-9a-zA-Z]{33}$")

	def __init__(self, data: bytes) -> None:
		super().__init__(data)

	def accept(self, visitor: AddressVisitor):
		visitor.visitDashBlockchainAddress(self)

	def as_string(self) -> str:
		address_data_encode: bytes = base58.b58encode(self._data)
		address_data_str: str = str(address_data_encode, 'UTF-8')
		return address_data_str
