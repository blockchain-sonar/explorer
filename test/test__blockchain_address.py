from unittest import TestCase

from blockchain_sonar_backend.blockchain_address import BlockchainAddress, BitcoinBlockchainAddress, Eip55BlockchainAddress

class TestBlockchainAddress(TestCase):
	def test__address_resolve__bitcoin_1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2(self):
		blockchain_address = BlockchainAddress.parse("1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2")
		self.assertIsInstance(blockchain_address, BitcoinBlockchainAddress, "Address 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 should be BitcoinBlockchainAddress")

	def test__address_resolve__ethereum_0xd3cda913deb6f67967b99d67acdfa1712c293601(self):
		blockchain_address = BlockchainAddress.parse("0xd3cda913deb6f67967b99d67acdfa1712c293601")
		self.assertIsNotNone(blockchain_address, "BlockchainAddress.parse should not return None")
		self.assertIsInstance(blockchain_address, Eip55BlockchainAddress, "Address 0xd3cda913deb6f67967b99d67acdfa1712c293601 should be Eip55BlockchainAddress")

		friendly_address: Eip55BlockchainAddress = blockchain_address

		reverse_legacy_address: str = friendly_address.to_legacy_address()
		self.assertEqual(reverse_legacy_address, "0xd3cda913deb6f67967b99d67acdfa1712c293601")

		reverse_eip55_address: str = friendly_address.to_eip55_address()
		self.assertEqual(reverse_eip55_address, "0xd3CdA913deB6f67967B99D67aCDFa1712C293601")

	def test__address_resolve__ethereum_0xd3CdA913deB6f67967B99D67aCDFa1712C293601(self):
		blockchain_address = BlockchainAddress.parse("0xd3CdA913deB6f67967B99D67aCDFa1712C293601")
		self.assertIsNotNone(blockchain_address, "BlockchainAddress.parse should not return None")
		self.assertIsInstance(blockchain_address, Eip55BlockchainAddress, "Address 0xd3CdA913deB6f67967B99D67aCDFa1712C293601 should be Eip55BlockchainAddress")

		friendly_address: Eip55BlockchainAddress = blockchain_address

		reverse_legacy_address: str = friendly_address.to_legacy_address()
		self.assertEqual(reverse_legacy_address, "0xd3cda913deb6f67967b99d67acdfa1712c293601")

		reverse_eip55_address: str = friendly_address.to_eip55_address()
		self.assertEqual(reverse_eip55_address, "0xd3CdA913deB6f67967B99D67aCDFa1712C293601")


