from unittest import TestCase

from blockchain_sonar_backend.blockchain_address import DashBlockchainAddress,Optional

class TestDashAddress(TestCase):
	def test__tron_addresses_should_be_25_bytes(self):
		address: DashBlockchainAddress = DashBlockchainAddress.parse("XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13")
		self.assertEqual(len(address.data), 25, "Bytes len of Litecoin should be 25")

	def test__litecoin_addresses_check_per_bytes(self):
		address: DashBlockchainAddress = DashBlockchainAddress.parse("XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13")
		address_data: bytes = address.data
		self.assertEqual(len(address_data), 25, "Bytes len of Litecoin should be 25")

		# According to https://appdevtools.com/base58-encoder-decoder
		# XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13
		# 4c e9 57 ae cb b4 5d b8 82 48 ec 03 e5 9e 57 60 26 d6 2c ad 78 e2 66 98 0e

		self.assertEqual(address_data[0], 0x4c, "1 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x4c")
		self.assertEqual(address_data[1], 0xe9, "2 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0xe9")
		self.assertEqual(address_data[2], 0x57, "3 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x57")
		self.assertEqual(address_data[3], 0xae, "4 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0xae")
		self.assertEqual(address_data[4], 0xcb, "5 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0xcb")
		self.assertEqual(address_data[5], 0xb4, "6 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0xb4")
		self.assertEqual(address_data[6], 0x5d, "7 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x5d")
		self.assertEqual(address_data[7], 0xb8, "8 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0xb8")
		self.assertEqual(address_data[8], 0x82, "9 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x82")
		self.assertEqual(address_data[9], 0x48, "10 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x48")
		self.assertEqual(address_data[10], 0xec, "11 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0xec")
		self.assertEqual(address_data[11], 0x03, "12 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x03")
		self.assertEqual(address_data[12], 0xe5, "13 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0xe5")
		self.assertEqual(address_data[13], 0x9e, "14 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x9e")
		self.assertEqual(address_data[14], 0x57, "15 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x57")
		self.assertEqual(address_data[15], 0x60, "16 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x60")
		self.assertEqual(address_data[16], 0x26, "17 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x26")
		self.assertEqual(address_data[17], 0xd6, "18 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0xd6")
		self.assertEqual(address_data[18], 0x2c, "19 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x2c")
		self.assertEqual(address_data[19], 0xad, "20 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0xad")
		self.assertEqual(address_data[20], 0x78, "21 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x08")
		self.assertEqual(address_data[21], 0xe2, "22 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0xe2")
		self.assertEqual(address_data[22], 0x66, "23 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x66")
		self.assertEqual(address_data[23], 0x98, "24 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x98")
		self.assertEqual(address_data[24], 0x0e, "25 byte of Dash address 'XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13' should be 0x0e")
	
	def test__dash_address_check_as_legacy(self):
		address: DashBlockchainAddress = DashBlockchainAddress.parse("XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13")
		chek_address = address.as_dash_address()
		self.assertEqual(chek_address, "XwxeKFtAXa9wGvX4QijQxz2yC4hMzfAa13")

	def test__tron_fake_address_try_parse(self):
		address: Optional[DashBlockchainAddress] = DashBlockchainAddress.try_parse("1")
		self.assertIsNone(address, "DashBlockchainAddress should return None")

	def test__dash_fake_address_parse(self):
		try:
			address: DashBlockchainAddress = DashBlockchainAddress.parse("1")
		except Exception as e:
			# TODO check for correct data address in e
			return
		self.fail("The method 'parse' returned Exception.")
