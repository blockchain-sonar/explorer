#
# See https://stackoverflow.com/questions/55248703/how-use-flask-route-with-class-based-view
#

from flask import Blueprint, Response, current_app, jsonify, request

from blockchain_sonar_backend.blockchain_address import BitcoinBlockchainAddress, BitcoincashBlockchainAddress, BlockchainAddress, BlockchainAddressVisitor, DashBlockchainAddress, DogecoinBlockchainAddress, EthereumBlockchainAddress, LitecoinBlockchainAddress, TronBlockchainAddress

class CurrencyResolverVisitor(BlockchainAddressVisitor):

	def __init__(self) -> None:
		super().__init__()
		self._currencies = []

	@property
	def currencies(self) -> list[str]:
		return self._currencies

	def visitBitcoinBlockchainAddress(self, address: BitcoinBlockchainAddress):
		raise Exception("Not implemented yet")

	def visitBitcoincashBlockchainAddress(self, address: BitcoincashBlockchainAddress):
		raise Exception("Not implemented yet")

	def visitDashBlockchainAddress(self, address: DashBlockchainAddress):
		raise Exception("Not implemented yet")

	def visitDogecoinBlockchainAddress(self, address: DogecoinBlockchainAddress):
		raise Exception("Not implemented yet")

	def visitEthereumBlockchainAddress(self, address: EthereumBlockchainAddress):
		self._currencies.append("ETH")
		self._currencies.append("USDT")
		self._currencies.append("BNB")

	def visitLitecoinBlockchainAddress(self, address: LitecoinBlockchainAddress):
		raise Exception("Not implemented yet")

	def visitTronBlockchainAddress(self, address: TronBlockchainAddress):
		raise Exception("Not implemented yet")


class ExplorerV1Controller(object):

	def __init__(self):
		self.blueprint = Blueprint('Explorer API', __name__)
		self.blueprint.add_url_rule('/', methods=["GET"], view_func=self._index)
		self.blueprint.add_url_rule('/asset', methods=["GET"], view_func=self._asset_list)
		self.blueprint.add_url_rule('/asset/<asset>', methods=["GET"], view_func=self._asset_fetch)
		self.blueprint.add_url_rule('/address/<address_str>', methods=["GET"], view_func=self._address)
		self.blueprint.add_url_rule('/transaction/<transaction>', methods=["GET"], view_func=self._transaction)

	#
	# Call this:
	#   curl --verbose --request GET --header 'Accept: */*' http://127.0.0.1:5000/explorer/v1/
	#
	def _index(self):
		return Response("See Explorer API documentation at https://docs.blockchain-sonar.com/explorer/\n", mimetype="text/plain")

	#
	# Call this:
	#   curl --verbose --request GET --header 'Accept: application/json' http://127.0.0.1:5000/explorer/v1/asset
	#
	def _asset_list(self):
		return Response('''{
	"ETH": {
		"name": "Ether"
	},
	"USDT": {
		"name": "Tether USD"
	},
	"BNB": {
		"name": "Binance Coin"
	},
	"BUSD-T": {
		"name": "BUSD-T Stablecoin"
	},
	"MATIC": {
		"name": "MATIC"
	}
}
''', mimetype="application/json")

	#
	# Call this:
	#   curl --verbose --request GET --header 'Accept: application/json' http://127.0.0.1:5000/explorer/v1/asset/ETH
	#
	def _asset_fetch(self, asset: str):
		return Response('''{
	"name": "Ether"
}
''', mimetype="application/json")

	#
	# Call this:
	#   curl --verbose --request GET --header 'Accept: application/json' http://127.0.0.1:5000/explorer/v1/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e
	#
	def _address(self, address_str: str):
		addresses: list[BlockchainAddress] = BlockchainAddress.parse(address_str)

		visitor = CurrencyResolverVisitor()

		for address in addresses:
			address.accept(visitor)

		currencies: list[str] = visitor.currencies


		return Response('''{
	"address": "0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	"assets": {
		"ETH": {
			"balance": null,
			"alternatives": {
				"com.blockchair": "https://blockchair.com/ethereum/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
				"com.blockcypher": "https://live.blockcypher.com/eth/address/2b6828f4f227953fb36f42bda830b457afdc1c5e/",
				"io.etherscan": "https://etherscan.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
				"io.ethplorer": "https://ethplorer.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
				"org.etherchain": "https://etherchain.org/account/2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		},
		"USDT": {
			"balance": null,
			"alternatives": {
				"io.etherscan": "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		},
		"BNB": {
			"balance": null,
			"alternatives": {
				"com.bscscan": "https://bscscan.com/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		},
		"BUSD-T": {
			"balance": null,
			"alternatives": {
				"com.bscscan": "https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		},
		,
		"MATIC": {
			"balance": null,
			"alternatives": {
				"com.polygonscan": "https://polygonscan.com/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		},
		
	}
}
''', mimetype="application/json")

	#
	# Call this:
	#   curl --verbose --request GET --header 'Accept: application/json' http://127.0.0.1:5000/explorer/v1/transaction/0x25eb25e730b5c0f805ec3695040b6c8a2e1ec68effc884c3ec5b7e6dd038d1a8
	#
	def _transaction(self, transaction: str):
		return Response('''{
	"transaction": "0x25eb25e730b5c0f805ec3695040b6c8a2e1ec68effc884c3ec5b7e6dd038d1a8",
	"assets": {
		"ETH": {
			"value": null,
			"alternatives": {
				"com.blockchair": "https://blockchair.com/ethereum/transaction/0x5db0654fc868ed8cd1655038a3ef7faadcb3f7d34d1cd5b649f9e217f311cf14",
				"com.blockcypher": "https://live.blockcypher.com/eth/tx/0x25eb25e730b5c0f805ec3695040b6c8a2e1ec68effc884c3ec5b7e6dd038d1a8/",
				"io.etherscan": "https://etherscan.io/tx/0x25eb25e730b5c0f805ec3695040b6c8a2e1ec68effc884c3ec5b7e6dd038d1a8",
				"io.ethplorer": "https://ethplorer.io/tx/0x25eb25e730b5c0f805ec3695040b6c8a2e1ec68effc884c3ec5b7e6dd038d1a8",
				"org.etherchain": "https://etherchain.org/tx/0x25eb25e730b5c0f805ec3695040b6c8a2e1ec68effc884c3ec5b7e6dd038d1a8"
			}
		},
		"USDT": {
			"value": null,
			"alternatives": {
				"io.etherscan": "https://etherscan.io/tx/0x25eb25e730b5c0f805ec3695040b6c8a2e1ec68effc884c3ec5b7e6dd038d1a8"
			}
		},
		"BNB": {
			"value": null,
			"alternatives": {
				"com.bscscan": "https://bscscan.com/tx/0x25eb25e730b5c0f805ec3695040b6c8a2e1ec68effc884c3ec5b7e6dd038d1a8"
			}
		},
		"BUSD-T": {
			"value": null,
			"alternatives": {
				"com.bscscan": "https://bscscan.com/tx/0x25eb25e730b5c0f805ec3695040b6c8a2e1ec68effc884c3ec5b7e6dd038d1a8"
			}
		},
		"MATIC": {
			"value": null,
			"alternatives": {
				"com.polygonscan": "https://polygonscan.com/tx/0x25eb25e730b5c0f805ec3695040b6c8a2e1ec68effc884c3ec5b7e6dd038d1a8"
			}
		}
	}
}
''', mimetype="application/json")
