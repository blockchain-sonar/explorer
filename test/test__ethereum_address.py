from unittest import TestCase

from blockchain_sonar_backend.blockchain_address import EthereumBlockchainAddress

class TestEthereumAddress(TestCase):
	def test__ethereum_address_should_be_20_bytes(self):
		address: EthereumBlockchainAddress = EthereumBlockchainAddress.parse("0xd3cda913deb6f67967b99d67acdfa1712c293601")
		self.assertEqual(len(address.data), 20, "Bytes len of Ethereum should be 20")

	def test__ethereum_address_check_per_bytes(self):
		address: EthereumBlockchainAddress = EthereumBlockchainAddress.parse("0xd3cda913deb6f67967b99d67acdfa1712c293601")
		address_data: bytes = address.data
		self.assertEqual(len(address_data), 20, "Bytes len of Ethereum should be 20")

		# d3 cd a9 13 de b6 f6 79 67 b9 9d 67 ac df a1 71 2c 29 36 01

		self.assertEqual(address_data[0], 0xd3, "1 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0xd3")
		self.assertEqual(address_data[1], 0xcd, "2 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0xcd")
		self.assertEqual(address_data[2], 0xa9, "3 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0xa9")
		self.assertEqual(address_data[3], 0x13, "4 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0x13")
		self.assertEqual(address_data[4], 0xde, "5 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0xde")
		self.assertEqual(address_data[5], 0xb6, "6 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0xb6")
		self.assertEqual(address_data[6], 0xf6, "7 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0xf6")
		self.assertEqual(address_data[7], 0x79, "8 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0x79")
		self.assertEqual(address_data[8], 0x67, "9 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0x67")
		self.assertEqual(address_data[9], 0xb9, "10 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0xb9")
		self.assertEqual(address_data[10], 0x9d, "11 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0x9d")
		self.assertEqual(address_data[11], 0x67, "12 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0x67")
		self.assertEqual(address_data[12], 0xac, "13 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0xac")
		self.assertEqual(address_data[13], 0xdf, "14 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0xdf")
		self.assertEqual(address_data[14], 0xa1, "15 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0xa1")
		self.assertEqual(address_data[15], 0x71, "16 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0x71")
		self.assertEqual(address_data[16], 0x2c, "17 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0x2c")
		self.assertEqual(address_data[17], 0x29, "18 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0x29")
		self.assertEqual(address_data[18], 0x36, "19 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0x36")
		self.assertEqual(address_data[19], 0x01, "20 byte of Ethereum address '0xd3cda913deb6f67967b99d67acdfa1712c293601' should be 0x01")
