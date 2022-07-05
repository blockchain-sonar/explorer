from unittest import TestCase

from blockchain_sonar_backend.blockchain_address import LitecoinBlockchainAddress,Optional

class TestDogecoinAddress(TestCase):
	def test__litecoin_addresses_should_be_25_bytes(self):
		address: LitecoinBlockchainAddress = LitecoinBlockchainAddress.parse("LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW")
		self.assertEqual(len(address.data), 25, "Bytes len of Litecoin should be 25")

	def test__litecoin_addresses_check_per_bytes(self):
		address: LitecoinBlockchainAddress = LitecoinBlockchainAddress.parse("LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW")
		address_data: bytes = address.data
		self.assertEqual(len(address_data), 25, "Bytes len of Litecoin should be 25")

		# According to https://appdevtools.com/base58-encoder-decoder
		# LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW
		# 30 74 14 5b c7 fb 89 f8 7b 27 31 f3 97 17 f4 ac 5f 89 2c 12 96 27 3f 6b fb

		self.assertEqual(address_data[0], 0x30, "1 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x30")
		self.assertEqual(address_data[1], 0x74, "2 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x74")
		self.assertEqual(address_data[2], 0x14, "3 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x14")
		self.assertEqual(address_data[3], 0x5b, "4 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x5b")
		self.assertEqual(address_data[4], 0xc7, "5 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0xc7")
		self.assertEqual(address_data[5], 0xfb, "6 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0xfb")
		self.assertEqual(address_data[6], 0x89, "7 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x89")
		self.assertEqual(address_data[7], 0xf8, "8 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0xf8")
		self.assertEqual(address_data[8], 0x7b, "9 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x7b")
		self.assertEqual(address_data[9], 0x27, "10 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x27")
		self.assertEqual(address_data[10], 0x31, "11 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x31")
		self.assertEqual(address_data[11], 0xf3, "12 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0xf3")
		self.assertEqual(address_data[12], 0x97, "13 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x97")
		self.assertEqual(address_data[13], 0x17, "14 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x17")
		self.assertEqual(address_data[14], 0xf4, "15 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0xf4")
		self.assertEqual(address_data[15], 0xac, "16 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0xac")
		self.assertEqual(address_data[16], 0x5f, "17 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x5f")
		self.assertEqual(address_data[17], 0x89, "18 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x89")
		self.assertEqual(address_data[18], 0x2c, "19 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x2c")
		self.assertEqual(address_data[19], 0x12, "20 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x12")
		self.assertEqual(address_data[20], 0x96, "21 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x96")
		self.assertEqual(address_data[21], 0x27, "22 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x27")
		self.assertEqual(address_data[22], 0x3f, "23 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x3f")
		self.assertEqual(address_data[23], 0x6b, "24 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0x6b")
		self.assertEqual(address_data[24], 0xfb, "25 byte of Litecoin address 'LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW' should be 0xfb")
	
	def test__dogecoin_address_check_as_legacy(self):
		address: LitecoinBlockchainAddress = LitecoinBlockchainAddress.parse("LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW")
		chek_address = address.as_address()
		self.assertEqual(chek_address, "LVoj2zxgNxe5qGuLxdUU2pKKGbgA4BgypW")

	def test__litecoin_fake_address_try_parse(self):
		address: Optional[LitecoinBlockchainAddress] = LitecoinBlockchainAddress.try_parse("1")
		self.assertIsNone(address, "LitecoinBlockchainAddress should return None")

	def test__litecoin_fake_address_parse(self):
		try:
			address: LitecoinBlockchainAddress = LitecoinBlockchainAddress.parse("1")
		except Exception as e:
			# TODO check for correct data address in e
			return
		self.fail("The method 'parse' returned Exception.")
