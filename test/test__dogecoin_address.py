from unittest import TestCase

from blockchain_sonar_backend.blockchain_address import DogecoinBlockchainAddress

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
		# TODO
		# TODO
		# TODO
