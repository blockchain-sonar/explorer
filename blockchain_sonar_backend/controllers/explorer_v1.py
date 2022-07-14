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
		self._currencies.append("Dash")

	def visitDogecoinBlockchainAddress(self, address: DogecoinBlockchainAddress):
		self._currencies.append("Dogecoin")

	def visitEthereumBlockchainAddress(self, address: EthereumBlockchainAddress):
		self._currencies.append("ETH")
		self._currencies.append("USDT")
		self._currencies.append("BNB")
		self._currencies.append("BUSD-T")
		self._currencies.append("MATIC")

	def visitLitecoinBlockchainAddress(self, address: LitecoinBlockchainAddress):
		self._currencies.append("LTC")

	def visitTronBlockchainAddress(self, address: TronBlockchainAddress):
		self._currencies.append("TRX")


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
		result = {
					"name": asset
				}
		# mimetype="application/json")
		return jsonify(result)

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

		short_address_str = address_str[2:]
		
		result = {
		"address": address_str,
		"assets": {
			"ETH": {
				"balance": None,
				"alternatives": {
					"com.blockchair": "https://blockchair.com/ethereum/address/%s" %address_str,
					"com.blockcypher": "https://live.blockcypher.com/eth/address/%s/" %short_address_str,
					"io.etherscan": "https://etherscan.io/address/%s" %address_str,
					"io.ethplorer": "https://ethplorer.io/address/%s" %address_str,
					"org.etherchain": "https://etherchain.org/account/%s" %short_address_str
				}
			},
			"USDT": {
				"balance": None,
				"alternatives": {
					"io.etherscan": "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7?a=%s" %address_str,
				}
			},
			"BNB": {
				"balance": None,
				"alternatives": {
					"com.bscscan": "https://bscscan.com/address/%s" %address_str,
				}
			},
			"BUSD-T": {
				"balance": None,
				"alternatives": {
					"com.bscscan": "https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955?a=%s" %address_str,
				}
			},
			
			"MATIC": {
				"balance": None,
				"alternatives": {
					"com.polygonscan": "https://polygonscan.com/address/%s" %address_str,
					
					}
				}
				
			}
		}
		#mimetype = "application/json"
		return jsonify(result)

	#
	# Call this:
	#   curl --verbose --request GET --header 'Accept: application/json' http://127.0.0.1:5000/explorer/v1/transaction/0x25eb25e730b5c0f805ec3695040b6c8a2e1ec68effc884c3ec5b7e6dd038d1a8
	#
	def _transaction(self, transaction: str):
		result = {
			"transaction": transaction,
			"assets": {
				"ETH": {
					"value": None,
					"alternatives": {
						"com.blockchair": "https://blockchair.com/ethereum/transaction/%s" %transaction,
						"com.blockcypher": "https://live.blockcypher.com/eth/tx/%s/" %transaction,
						"io.etherscan": "https://etherscan.io/tx/%s" %transaction,
						"io.ethplorer": "https://ethplorer.io/tx/%s" %transaction,
						"org.etherchain": "https://etherchain.org/tx/%s" %transaction
					}
				},
				"USDT": {
					"value": None,
					"alternatives": {
						"io.etherscan": "https://etherscan.io/tx/%s" %transaction
					}
				},
				"BNB": {
					"value": None,
					"alternatives": {
						"com.bscscan": "https://bscscan.com/tx/%s" %transaction
					}
				},
				"BUSD-T": {
					"value": None,
					"alternatives": {
						"com.bscscan": "https://bscscan.com/tx/%s" %transaction
					}
				},
				"MATIC": {
					"value": None,
					"alternatives": {
						"com.polygonscan": "https://polygonscan.com/tx/%s" %transaction
					}
				}
			}
		}
		#mimetype="application/json"
		return jsonify(result)
