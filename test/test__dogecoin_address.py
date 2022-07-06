from unittest import TestCase

from blockchain_sonar_backend.blockchain_address import DogecoinBlockchainAddress,Optional

class TestDogecoinAddress(TestCase):
	def test__dogecoin_address_should_be_25_bytes(self):
		address: DogecoinBlockchainAddress = DogecoinBlockchainAddress.parse("DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k")
		self.assertEqual(len(address.data), 25, "Bytes len of Dogecoin should be 25")

	def test__dogecoin_address_check_per_bytes(self):
		address: DogecoinBlockchainAddress = DogecoinBlockchainAddress.parse("DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k")
		address_data: bytes = address.data
		self.assertEqual(len(address_data), 25, "Bytes len of Dogecoin should be 25")

		# According to https://appdevtools.com/base58-encoder-decoder
		# DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k
		# 1e de bd 3b 7e 9a fb b3 ab e0 cc f3 a0 22 ec 90 95 13 07 50 1d 8c 1a da 37

		self.assertEqual(address_data[0], 0x1e, "1 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x1e")
		self.assertEqual(address_data[1], 0xde, "2 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0xde")
		self.assertEqual(address_data[2], 0xbd, "3 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0xbd")
		self.assertEqual(address_data[3], 0x3b, "4 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x3b")
		self.assertEqual(address_data[4], 0x7e, "5 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x7e")
		self.assertEqual(address_data[5], 0x9a, "6 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x9a")
		self.assertEqual(address_data[6], 0xfb, "7 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0xfb")
		self.assertEqual(address_data[7], 0xb3, "8 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0xb3")
		self.assertEqual(address_data[8], 0xab, "9 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0xab")
		self.assertEqual(address_data[9], 0xe0, "10 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0xe0")
		self.assertEqual(address_data[10], 0xcc, "11 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0xcc")
		self.assertEqual(address_data[11], 0xf3, "12 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0xf3")
		self.assertEqual(address_data[12], 0xa0, "13 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0xa0")
		self.assertEqual(address_data[13], 0x22, "14 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x22")
		self.assertEqual(address_data[14], 0xec, "15 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0xec")
		self.assertEqual(address_data[15], 0x90, "16 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x90")
		self.assertEqual(address_data[16], 0x95, "17 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x95")
		self.assertEqual(address_data[17], 0x13, "18 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x13")
		self.assertEqual(address_data[18], 0x07, "19 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x07")
		self.assertEqual(address_data[19], 0x50, "20 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x50")
		self.assertEqual(address_data[20], 0x1d, "21 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x1d")
		self.assertEqual(address_data[21], 0x8c, "22 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x8c")
		self.assertEqual(address_data[22], 0x1a, "23 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x1a")
		self.assertEqual(address_data[23], 0xda, "24 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0xda")
		self.assertEqual(address_data[24], 0x37, "25 byte of Dogecoin address 'DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k' should be 0x37")
	
	def test__dogecoin_address_check_as_legacy(self):
		address: DogecoinBlockchainAddress = DogecoinBlockchainAddress.parse("DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k")
		chek_address = address.as_dogecoin_address()
		self.assertEqual(chek_address, "DRSqEwcnJX3GZWH9Twtwk8D5ewqdJzi13k")

	def test__dogecoin_fake_address_try_parse(self):
		address: Optional[DogecoinBlockchainAddress] = DogecoinBlockchainAddress.try_parse("1")
		self.assertIsNone(address, "DogecoinBlockchainAddress should return None")

	def test__dogecoin_fake_address_parse(self):
		try:
			address: DogecoinBlockchainAddress = DogecoinBlockchainAddress.parse("1")
		except Exception as e:
			# TODO check for correct data address in e
			return
		self.fail("The method 'parse' returned Exception.")
