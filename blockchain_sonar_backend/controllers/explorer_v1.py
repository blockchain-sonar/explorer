#
# See https://stackoverflow.com/questions/55248703/how-use-flask-route-with-class-based-view
#

from ast import Assert
from flask import Blueprint, Response, current_app, jsonify, request
from blockchain_sonar_backend.blockchain import Blockchain

from blockchain_sonar_backend.blockchain_address import BitcoinBlockchainAddress, BitcoincashBlockchainAddress, BlockchainAddress, BlockchainAddressVisitor, DashBlockchainAddress, DogecoinBlockchainAddress, EthereumBlockchainAddress, LitecoinBlockchainAddress, TronBlockchainAddress
from blockchain_sonar_backend.asset import ETH, USDT, BNB, BUSDT, MATIC, Asset

class AssetResolverVisitor(BlockchainAddressVisitor):

	def __init__(self) -> None:
		super().__init__()
		self._assets = []

	@property
	def assets(self) -> list[Asset]:
		return self._assets

	def visitBitcoinBlockchainAddress(self, address: BitcoinBlockchainAddress):
		raise Exception("Not implemented yet")

	def visitBitcoincashBlockchainAddress(self, address: BitcoincashBlockchainAddress):
		raise Exception("Not implemented yet")

	def visitDashBlockchainAddress(self, address: DashBlockchainAddress):
		raise Exception("Not implemented yet")
		# self._assets.append(DASH)

	def visitDogecoinBlockchainAddress(self, address: DogecoinBlockchainAddress):
		raise Exception("Not implemented yet")
		# self._assets.append(DOGE)

	def visitEthereumBlockchainAddress(self, address: EthereumBlockchainAddress):
		self._assets.append(ETH)
		self._assets.append(USDT)
		self._assets.append(BNB)
		self._assets.append(BUSDT)
		self._assets.append(MATIC)

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
		from blockchain_sonar_backend.asset import Asset
		asset = Asset()
		list_asset = asset.asset_dict
		return jsonify(list_asset) 

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

		visitor = AssetResolverVisitor()

		for address in addresses:
			address.accept(visitor)

		assets_data = {}

		# {
		# 	"ETH": {
		# 		"balance": None,
		# 		"alternatives": {
		# 			"com.blockchair": "https://blockchair.com/ethereum/address/%s" %address_str,
		# 			"com.blockcypher": "https://live.blockcypher.com/eth/address/%s/" %changed_address_str,
		# 			"io.etherscan": "https://etherscan.io/address/%s" %address_str,
		# 			"io.ethplorer": "https://ethplorer.io/address/%s" %address_str,
		# 			"org.etherchain": "https://etherchain.org/account/%s" %changed_address_str
		# 		}
		# 	},
		# 	"USDT": {
		# 		"balance": None,
		# 		"alternatives": {
		# 			"io.etherscan": "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7?a=%s" %address_str,
		# 		}
		# 	},
		# 	"BNB": {
		# 		"balance": None,
		# 		"alternatives": {
		# 			"com.bscscan": "https://bscscan.com/address/%s" %address_str,
		# 		}
		# 	},
		# 	"BUSD-T": {
		# 		"balance": None,
		# 		"alternatives": {
		# 			"com.bscscan": "https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955?a=%s" %address_str,
		# 		}
		# 	},
			
		# 	"MATIC": {
		# 		"balance": None,
		# 		"alternatives": {
		# 			"com.polygonscan": "https://polygonscan.com/address/%s" %address_str,
					
		# 			}
		# 		}
				
		# 	}

		assets: list[Asset] = visitor.assets
		for asset in assets:
			asset_data = {
				"name": asset.name,
				"balance": None,
				"alternatives": {}
			}

			blockchain_data = []
			for blockchain_representation in asset.blockchains:
				blockchain: Blockchain = blockchain_representation.blockchain
				blockchain_data.append({
					"blockchain": blockchain.name,
					"token": blockchain.is_token
				})

			asset_data["blockchains"] = blockchain_data

			assets_data[asset.code] = asset_data

		result = {
			"address": address_str,
			"assets": assets_data
		}

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
