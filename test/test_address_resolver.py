from unittest import TestCase

from blockchain_sonar_backend.address_resolver import address_resolve
from blockchain_sonar_backend.blockchain_address import BlockchainAddress

class TestAddressResolver(TestCase):
	def test__address_resolve__bitcoin_1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2(self):
		result = address_resolve(BlockchainAddress.parse("1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"))
		self.assertIn("bitcoin", result, "Address 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 should be bitcoin")
		self.assertNotIn("ethereum", result, "Address 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 should not be ethereum")

	def test__address_resolve__ethereum_0xd3cda913deb6f67967b99d67acdfa1712c293601(self):
		result = address_resolve(BlockchainAddress.parse("0xd3cda913deb6f67967b99d67acdfa1712c293601"))
		self.assertIn("ethereum", result, "Address 0xd3cda913deb6f67967b99d67acdfa1712c293601 should be ethereum")
		self.assertNotIn("bitcoin", result, "Address 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 should not be bitcoin")
		

