#
# See https://stackoverflow.com/questions/55248703/how-use-flask-route-with-class-based-view
#

from flask import Blueprint, Response, jsonify
from blockchain_sonar_backend.blockchain import Blockchain

from blockchain_sonar_backend.address import BitcoinBlockchainAddress, BitcoincashBlockchainAddress, Address, AddressVisitor, DashBlockchainAddress, DogecoinBlockchainAddress, EthereumBlockchainAddress, LitecoinBlockchainAddress, TronBlockchainAddress
from blockchain_sonar_backend.asset import ETH, USDT, BNB, BUSDT, MATIC, Dash, Dogecoin, Tron, Litecoin, Asset, AssetTokenRepresentationExplorer
from blockchain_sonar_backend.explorer import Explorer

class AssetResolverVisitor(AddressVisitor):

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
		self._assets.append(Dash)

	def visitDogecoinBlockchainAddress(self, address: DogecoinBlockchainAddress):
		self._assets.append(Dogecoin)

	def visitEthereumBlockchainAddress(self, address: EthereumBlockchainAddress):
		self._assets.append(ETH)
		self._assets.append(USDT)
		self._assets.append(BNB)
		self._assets.append(BUSDT)
		self._assets.append(MATIC)

	def visitLitecoinBlockchainAddress(self, address: LitecoinBlockchainAddress):
		self._assets.append(Litecoin)

	def visitTronBlockchainAddress(self, address: TronBlockchainAddress):
		self._assets.append(Tron)


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
	#   curl --verbose --request GET --header 'Accept: application/json' http://127.0.0.1:5000/explorer/v1/address/DQvuJB3eHEUmdB2wi2K9B6Vdimq9DNJU7Z
	# {
	# 	"address": "0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 	"assets": {
	# 		"BNB": {
	# 			"alternatives": {
	# 				"com.bscscan": "https://bscscan.com/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 				"io.binance.mintscan": "https://binance.mintscan.io/account/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 				"io.etherscan": "https://etherscan.io/token/0xB8c77482e45F1F44dE1745F52C74426C631bDD52?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 				"io.explorer.bitquery": "https://explorer.bitquery.io/bsc/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
	# 			},
	# 			"balance": null,
	# 			"blockchains": [
	# 				{
	# 					"blockchain": "Binance Coin",
	# 					"token": false
	# 				},
	# 				{
	# 					"blockchain": "Ethereum",
	# 					"token": true
	# 				}
	# 			],
	# 			"name": "Binance Coin"
	# 		},
	# 		"BUSD-T": {
	# 			"alternatives": {
	# 				"com.bscscan": "https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 				"io.explorer.bitquery": "https://explorer.bitquery.io/bsc/token/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
	# 			},
	# 			"balance": null,
	# 			"blockchains": [
	# 				{
	# 					"blockchain": "Ethereum",
	# 					"token": true
	# 				}
	# 			],
	# 			"name": "BUSD Token"
	# 		},
	# 		"ETH": {
	# 			"alternatives": {
	# 				"com.bscscan": "https://bscscan.com/token/0x2170ed0880ac9a755fd29b2688956bd959f933f8?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 				"io.etherscan": "https://etherscan.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 				"io.ethplorer": "https://ethplorer.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 				"org.etherchain": "https://etherchain.org/account/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
	# 			},
	# 			"balance": null,
	# 			"blockchains": [
	# 				{
	# 					"blockchain": "Ethereum",
	# 					"token": false
	# 				},
	# 				{
	# 					"blockchain": "Binance Coin",
	# 					"token": true
	# 				}
	# 			],
	# 			"name": "Ether"
	# 		},
	# 		"MATIC": {
	# 			"alternatives": {
	# 				"com.blockchain": "https://blockchair.com/ethereum/erc-20/token/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 				"com.polygonscan": "https://polygonscan.com/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 				"io.explorer.bitquery": "https://explorer.bitquery.io/matic/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
	# 			},
	# 			"balance": null,
	# 			"blockchains": [
	# 				{
	# 					"blockchain": "Ethereum",
	# 					"token": true
	# 				},
	# 				{
	# 					"blockchain": "Polygon",
	# 					"token": false
	# 				}
	# 			],
	# 			"name": "Polygon"
	# 		},
	# 		"USDT": {
	# 			"alternatives": {
	# 				"io.etherscan": "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 				"io.ethplorer": "https://ethplorer.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 				"org.etherchain": "https://etherchain.org/account/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	# 				"org.tronscan": "https://tronscan.org/#/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e/"
	# 			},
	# 			"balance": null,
	# 			"blockchains": [
	# 				{
	# 					"blockchain": "Ethereum",
	# 					"token": true
	# 				},
	# 				{
	# 					"blockchain": "Tron",
	# 					"token": true
	# 				}
	# 			],
	# 			"name": "Tether"
	# 		}
	# 	}
	# }
	#
	def _address(self, address_str: str):
		addresses: list[Address] = Address.parse(address_str)

		visitor = AssetResolverVisitor()

		for address in addresses:
			address.accept(visitor)

		assets_data = {}

		assets: list[Asset] = visitor.assets
		for asset in assets:
			asset_data = {
				"name": asset.name,
				"balance": None,
				"alternatives": {}
			}

			blockchain_data = []
			alternatives_data = {}

			for blockchain_representation in asset.blockchain_representations:
				blockchain: Blockchain = blockchain_representation.blockchain
				is_token = blockchain_representation.is_token
				blockchain_data.append({
					"blockchain": blockchain.name,
					"token": is_token
				})

				for explorer_representation in blockchain_representation.explorer_representations:
					explorer: Explorer = explorer_representation.explorer

					if is_token and isinstance(explorer_representation, AssetTokenRepresentationExplorer):
						url_template: str = explorer_representation.token_url_template
					else:
						url_template: str = explorer_representation.address_url_template

					explorer_code = explorer.name
					address_url: str = url_template % address_str
					alternatives_data[explorer_code] = address_url

			asset_data["blockchains"] = blockchain_data
			asset_data["alternatives"] = alternatives_data

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
