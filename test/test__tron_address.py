from unittest import TestCase

from blockchain_sonar_backend.blockchain_address import TronBlockchainAddress,Optional

class TestTronAddress(TestCase):
	def test__tron_addresses_should_be_25_bytes(self):
		address: TronBlockchainAddress = TronBlockchainAddress.parse("TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL")
		self.assertEqual(len(address.data), 25, "Bytes len of Litecoin should be 25")

	def test__litecoin_addresses_check_per_bytes(self):
		address: TronBlockchainAddress = TronBlockchainAddress.parse("TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL")
		address_data: bytes = address.data
		self.assertEqual(len(address_data), 25, "Bytes len of Litecoin should be 25")

		# According to https://appdevtools.com/base58-encoder-decoder
		# TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL
		# 41 88 40 e6 c5 5b 9a da 32 6d 21 1d 81 8c 34 a9 94 ae ce d8 08 a3 f8 47 9d

		self.assertEqual(address_data[0], 0x41, "1 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x41")
		self.assertEqual(address_data[1], 0x88, "2 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x88")
		self.assertEqual(address_data[2], 0x40, "3 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x40")
		self.assertEqual(address_data[3], 0xe6, "4 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0xe6")
		self.assertEqual(address_data[4], 0xc5, "5 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0xc5")
		self.assertEqual(address_data[5], 0x5b, "6 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x5b")
		self.assertEqual(address_data[6], 0x9a, "7 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x9a")
		self.assertEqual(address_data[7], 0xda, "8 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0xda")
		self.assertEqual(address_data[8], 0x32, "9 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x32")
		self.assertEqual(address_data[9], 0x6d, "10 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x6d")
		self.assertEqual(address_data[10], 0x21, "11 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x21")
		self.assertEqual(address_data[11], 0x1d, "12 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x1d")
		self.assertEqual(address_data[12], 0x81, "13 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x81")
		self.assertEqual(address_data[13], 0x8c, "14 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x8c")
		self.assertEqual(address_data[14], 0x34, "15 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x34")
		self.assertEqual(address_data[15], 0xa9, "16 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0xa9")
		self.assertEqual(address_data[16], 0x94, "17 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x94")
		self.assertEqual(address_data[17], 0xae, "18 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0xae")
		self.assertEqual(address_data[18], 0xce, "19 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0xce")
		self.assertEqual(address_data[19], 0xd8, "20 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0xd8")
		self.assertEqual(address_data[20], 0x08, "21 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x08")
		self.assertEqual(address_data[21], 0xa3, "22 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0xa3")
		self.assertEqual(address_data[22], 0xf8, "23 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0xf8")
		self.assertEqual(address_data[23], 0x47, "24 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x47")
		self.assertEqual(address_data[24], 0x9d, "25 byte of Tron address 'TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL' should be 0x9d")
	
	def test__tron_address_check_as_legacy(self):
		address: TronBlockchainAddress = TronBlockchainAddress.parse("TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL")
		chek_address = address.as_tron_address()
		self.assertEqual(chek_address, "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL")

	def test__tron_fake_address_try_parse(self):
		address: Optional[TronBlockchainAddress] = TronBlockchainAddress.try_parse("1")
		self.assertIsNone(address, "TronBlockchainAddress should return None")

	def test__tron_fake_address_parse(self):
		try:
			address: TronBlockchainAddress = TronBlockchainAddress.parse("1")
		except Exception as e:
			# TODO check for correct data address in e
			return
		self.fail("The method 'parse' returned Exception.")
