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
		# TODO
		# TODO
		# TODO
