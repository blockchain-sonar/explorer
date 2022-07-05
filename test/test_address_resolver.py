from unittest import TestCase

from blockchain_sonar_backend.blockchain_resolver import blockchain_resolve
from blockchain_sonar_backend.blockchain_address import BlockchainAddress

class TestAddressResolver(TestCase):
	def test__address_resolve__bitcoin_1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2(self):
		blockchain_address = BlockchainAddress.parse("1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2")[0]
		result = blockchain_resolve(blockchain_address)
		self.assertIn("bitcoin", result, "Address 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 should be bitcoin")
		self.assertNotIn("ethereum", result, "Address 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 should not be ethereum")
		self.assertNotIn("dogecoin", result, "Address DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k should be dogecoin")
		self.assertNotIn("litecoin", result, "Address LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW should not be litecoin")

	def test__address_resolve__ethereum_0xd3cda913deb6f67967b99d67acdfa1712c293601(self):
		blockchain_address = BlockchainAddress.parse("0xd3cda913deb6f67967b99d67acdfa1712c293601")[0]
		result = blockchain_resolve(blockchain_address)
		self.assertIn("ethereum", result, "Address 0xd3cda913deb6f67967b99d67acdfa1712c293601 should be ethereum")
		self.assertNotIn("bitcoin", result, "Address 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 should not be bitcoin")
		self.assertNotIn("dogecoin", result, "Address DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k should be dogecoin")
		self.assertNotIn("litecoin", result, "Address LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW should not be litecoin")
		
	def test__address_resolve__dogecoin_DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k(self):
		blockchain_address = BlockchainAddress.parse("DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k")[0]
		result = blockchain_resolve(blockchain_address)
		self.assertIn("dogecoin", result, "Address DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k should be dogecoin")
		self.assertNotIn("bitcoin", result, "Address 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 should not be bitcoin")
		self.assertNotIn("ethereum", result, "Address 0xd3cda913deb6f67967b99d67acdfa1712c293601 should not be ethereum")
		self.assertNotIn("litecoin", result, "Address LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW should not be litecoin")

	def test__address_resolve__litecoin_LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW(self):
		blockchain_address = BlockchainAddress.parse("LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW")[0]
		result = blockchain_resolve(blockchain_address)
		self.assertIn("litecoin", result, "Address LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW should be litecoin")
		self.assertNotIn("dogecoin", result, "Address DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k should not be dogecoin")
		self.assertNotIn("bitcoin", result, "Address 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 should not be bitcoin")
		self.assertNotIn("ethereum", result, "Address 0xd3cda913deb6f67967b99d67acdfa1712c293601 should not be ethereum")
