class Asset:
	def __init__(self) -> None:
		pass
	@property
	def asset_dict(self):
		self.dict = {
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
		return self.dict
