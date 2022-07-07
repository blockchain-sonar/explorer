from unittest import TestCase

from blockchain_sonar_backend.blockchain_address import BitcoincashBlockchainAddress, BlockchainAddress, BitcoinBlockchainAddress, EthereumBlockchainAddress,DogecoinBlockchainAddress, LitecoinBlockchainAddress, TronBlockchainAddress, DashBlockchainAddress
from blockchain_sonar_backend.utils.collections import filter_type_single, filter_type_single_or_none



class TestBlockchainAddress(TestCase):
	def test__address_resolve__bitcoin_1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2(self):
		blockchain_addresses = BlockchainAddress.parse("1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2")
		self.assertIsNotNone(blockchain_addresses, "BlockchainAddress.parse('1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2') should not return None")
		self.assertIsInstance(blockchain_addresses, list, "BlockchainAddress.parse('1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2') should return list")

		bitcoin_blockchain_address: BitcoinBlockchainAddress = filter_type_single_or_none(BitcoinBlockchainAddress, blockchain_addresses)
		self.assertIsNotNone(bitcoin_blockchain_address, "BlockchainAddress.parse('1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2') should represent BitcoinBlockchainAddress")

	def test__address_resolve__bitcoincash_1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2(self):
		blockchain_addresses = BlockchainAddress.parse("1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2")
		self.assertIsNotNone(blockchain_addresses, "BlockchainAddress.parse('1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2') should not return None")
		self.assertIsInstance(blockchain_addresses, list, "BlockchainAddress.parse('1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2') should return list")
	
		bitcoincash_blockchain_address = filter_type_single_or_none(BitcoincashBlockchainAddress, blockchain_addresses)
		self.assertIsNotNone(bitcoincash_blockchain_address, "BlockchainAddress.parse('1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2') should represent BitcoincashBlockchainAddress")

	def test__address_resolve__ethereum_legacy_as_legacy_address(self):
		"""
		In the test we parse legacy format address "0xd3cda913deb6f67967b99d67acdfa1712c293601"
		and trying to represent it as_legacy_address
		"""
		blockchain_addresses = BlockchainAddress.parse("0xd3cda913deb6f67967b99d67acdfa1712c293601")
		self.assertIsNotNone(blockchain_addresses, "BlockchainAddress.parse('0xd3cda913deb6f67967b99d67acdfa1712c293601') should not return None")
		self.assertIsInstance(blockchain_addresses, list, "BlockchainAddress.parse('0xd3cda913deb6f67967b99d67acdfa1712c293601') should return list")
		self.assertEqual(len(blockchain_addresses), 1, "BlockchainAddress.parse('0xd3cda913deb6f67967b99d67acdfa1712c293601') should return list with single element")
	
		ethereum_blockchain_address = filter_type_single_or_none(EthereumBlockchainAddress, blockchain_addresses)
		self.assertIsNotNone(ethereum_blockchain_address, "BlockchainAddress.parse('0xd3cda913deb6f67967b99d67acdfa1712c293601') should represent EthereumBlockchainAddress")

		reverse_legacy_address: str = ethereum_blockchain_address.as_legacy_address()
		self.assertEqual(reverse_legacy_address, "0xd3cda913deb6f67967b99d67acdfa1712c293601")

	def test__address_resolve__ethereum_legacy_as_eip55_address(self):
		"""
		In the test we parse legacy format address "0xd3cda913deb6f67967b99d67acdfa1712c293601"
		and trying to represent it as_eip55_address
		"""
		blockchain_addresses = BlockchainAddress.parse("0xd3cda913deb6f67967b99d67acdfa1712c293601")
		self.assertIsNotNone(blockchain_addresses, "BlockchainAddress.parse('0xd3cda913deb6f67967b99d67acdfa1712c293601') should not return None")
		self.assertIsInstance(blockchain_addresses, list, "BlockchainAddress.parse('0xd3cda913deb6f67967b99d67acdfa1712c293601') should return list")
		self.assertEqual(len(blockchain_addresses), 1, "BlockchainAddress.parse('0xd3cda913deb6f67967b99d67acdfa1712c293601') should return list with single element")
	
		ethereum_blockchain_address = filter_type_single_or_none(EthereumBlockchainAddress, blockchain_addresses)
		self.assertIsNotNone(ethereum_blockchain_address, "BlockchainAddress.parse('0xd3cda913deb6f67967b99d67acdfa1712c293601') should represent EthereumBlockchainAddress")

		reverse_eip55_address: str = ethereum_blockchain_address.as_eip55_address()
		self.assertEqual(reverse_eip55_address, "0xd3CdA913deB6f67967B99D67aCDFa1712C293601")

	def test__address_resolve__ethereum_eip55_as_legacy_address(self):
		"""
		In the test we parse EIP-55 format address "0xd3cda913deb6f67967b99d67acdfa1712c293601"
		and trying to represent it as_legacy_address
		"""
		blockchain_addresses = BlockchainAddress.parse("0xd3CdA913deB6f67967B99D67aCDFa1712C293601")
		self.assertIsNotNone(blockchain_addresses, "BlockchainAddress.parse('0xd3CdA913deB6f67967B99D67aCDFa1712C293601') should not return None")
		self.assertIsInstance(blockchain_addresses, list, "BlockchainAddress.parse('0xd3CdA913deB6f67967B99D67aCDFa1712C293601') should return list")
		self.assertEqual(len(blockchain_addresses), 1, "BlockchainAddress.parse('0xd3CdA913deB6f67967B99D67aCDFa1712C293601') should return list with single element")
	
		ethereum_blockchain_address = filter_type_single_or_none(EthereumBlockchainAddress, blockchain_addresses)
		self.assertIsNotNone(ethereum_blockchain_address, "BlockchainAddress.parse('0xd3CdA913deB6f67967B99D67aCDFa1712C293601') should represent EthereumBlockchainAddress")

		reverse_legacy_address: str = ethereum_blockchain_address.as_legacy_address()
		self.assertEqual(reverse_legacy_address, "0xd3cda913deb6f67967b99d67acdfa1712c293601")

	def test__address_resolve__ethereum_eip55_as_eip55_address(self):
		"""
		In the test we parse EIP-55 format address "0xd3cda913deb6f67967b99d67acdfa1712c293601"
		and trying to represent it as_eip55_address
		"""
		blockchain_addresses = BlockchainAddress.parse("0xd3CdA913deB6f67967B99D67aCDFa1712C293601")
		self.assertIsNotNone(blockchain_addresses, "BlockchainAddress.parse('0xd3CdA913deB6f67967B99D67aCDFa1712C293601') should not return None")
		self.assertIsInstance(blockchain_addresses, list, "BlockchainAddress.parse('0xd3CdA913deB6f67967B99D67aCDFa1712C293601') should return list")
		self.assertEqual(len(blockchain_addresses), 1, "BlockchainAddress.parse('0xd3CdA913deB6f67967B99D67aCDFa1712C293601') should return list with single element")
	
		ethereum_blockchain_address = filter_type_single_or_none(EthereumBlockchainAddress, blockchain_addresses)
		self.assertIsNotNone(ethereum_blockchain_address, "BlockchainAddress.parse('0xd3CdA913deB6f67967B99D67aCDFa1712C293601') should represent EthereumBlockchainAddress")

		reverse_eip55_address: str = ethereum_blockchain_address.as_eip55_address()
		self.assertEqual(reverse_eip55_address, "0xd3CdA913deB6f67967B99D67aCDFa1712C293601")

	def test__address_resolve__dogecoin_as_dogecoin_address(self):
		"""
		In the test we parse Dogecoin format address "DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k"
		and trying to represent it as_dogecoin_address
		"""
		blockchain_addresses = BlockchainAddress.parse("DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k")
		self.assertIsNotNone(blockchain_addresses, "BlockchainAddress.parse('DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k') should not return None")
		self.assertIsInstance(blockchain_addresses, list, "BlockchainAddress.parse('DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k') should return list")
		self.assertEqual(len(blockchain_addresses), 1, "BlockchainAddress.parse('DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k') should return list with single element")
	
		dogecoin_blockchain_address = filter_type_single_or_none(DogecoinBlockchainAddress, blockchain_addresses)
		self.assertIsNotNone(dogecoin_blockchain_address, "BlockchainAddress.parse('DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k') should represent DogecoinBlockchainAddress")

		reverse_dogecoin_address: str = dogecoin_blockchain_address.as_string()
		self.assertEqual (reverse_dogecoin_address, "DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k")
	
	def test__address_resolve__litecoin_as_litecoin_address(self):
		"""
		In the test we parse Litecoin format address "LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW"
		and trying to represent it as_litecoin_address
		"""
		blockchain_addresses = BlockchainAddress.parse("LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW")
		self.assertIsNotNone(blockchain_addresses, "BlockchainAddress.parse('LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW') should not return None")
		self.assertIsInstance(blockchain_addresses, list, "BlockchainAddress.parse('LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW') should return list")
		self.assertEqual(len(blockchain_addresses), 1, "BlockchainAddress.parse('LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW') should return list with single element")
	
		litecoin_blockchain_address = filter_type_single_or_none(LitecoinBlockchainAddress, blockchain_addresses)
		self.assertIsNotNone(litecoin_blockchain_address, "BlockchainAddress.parse('LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW') should represent LitecoinBlockchainAddress")

		reverse_litecoin_address: str = litecoin_blockchain_address.as_string()
		self.assertEqual (reverse_litecoin_address, "LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW")

	def test__address_resolve__tron_as_tron_address(self):
		"""
		In the test we parse Tron format address "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL"
		and trying to represent it as_tron_address
		"""
		blockchain_addresses = BlockchainAddress.parse("TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL")
		self.assertIsNotNone(blockchain_addresses, "BlockchainAddress.parse('TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL') should not return None")
		self.assertIsInstance(blockchain_addresses, list, "BlockchainAddress.parse('TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL') should return list")
		self.assertEqual(len(blockchain_addresses), 1, "BlockchainAddress.parse('TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL') should return list with single element")
	
		tron_blockchain_address = filter_type_single_or_none(TronBlockchainAddress, blockchain_addresses)
		self.assertIsNotNone(tron_blockchain_address, "BlockchainAddress.parse('TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL') should represent TronBlockchainAddress")

		reverse_tron_address: str = tron_blockchain_address.as_string()
		self.assertEqual (reverse_tron_address, "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL")

	def test__address_resolve__dash_as_dash_address(self):
		"""
		In the test we parse Dash format address "XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13"
		and trying to represent it as_dash_address
		"""
		blockchain_addresses = BlockchainAddress.parse("XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13")
		self.assertIsNotNone(blockchain_addresses, "BlockchainAddress.parse('XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13') should not return None")
		self.assertIsInstance(blockchain_addresses, list, "BlockchainAddress.parse('XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13') should return list")
		self.assertEqual(len(blockchain_addresses), 1, "BlockchainAddress.parse('XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13') should return list with single element")
	
		tron_blockchain_address = filter_type_single_or_none(DashBlockchainAddress, blockchain_addresses)
		self.assertIsNotNone(tron_blockchain_address, "BlockchainAddress.parse('XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13') should represent DashBlockchainAddress")

		reverse_tron_address: str = tron_blockchain_address.as_string()
		self.assertEqual (reverse_tron_address, "XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13")
