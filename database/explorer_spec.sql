CREATE SEQUENCE "explorer_spec_id_seq" START 1;

CREATE TABLE "explorer_spec" (
    "id"            BIGINT PRIMARY KEY          NOT NULL    DEFAULT NEXTVAL('explorer_spec_id_seq'),
    "explorer_id" BIGINT                      NOT NULL,
    "explorer_url"  CHARACTER VARYING(200)      NOT NULL,
    "tx_url"        CHARACTER VARYING(300)      NOT NULL,
    "address_url"   CHARACTER VARYING(300)      NOT NULL,
    "token_url"     CHARACTER VARYING(300),
    "block_url"     CHARACTER VARYING(300)      NOT NULL,
    "blockchain_id" BIGINT                      NOT NULL,
    CONSTRAINT "fk__explorer_spec__blockchain" FOREIGN KEY ("blockchain_id") REFERENCES "blockchain" ("id")
);

INSERT INTO public.explorer(
	explorer_id, explorer_url, tx_url, address_url, token_url, block_url, blockchain_id)
	VALUES 
(1, 'https://www.blockchain.com/en/', 'https://www.blockchain.com/explorer/transactions/btc/{0}', 'https://www.blockchain.com/explorer/addresses/btc/{0}', 'https://www.blockchain.com/explorer/blocks/btc/{0}', 1),	
(1, 'https://www.blockchain.com/en/', 'https://www.blockchain.com/explorer/transactions/eth/{0}', 'https://www.blockchain.com/explorer/addresses/eth/{0}', 'https://www.blockchain.com/explorer/blocks/eth/{0}', 1),	
(1, 'https://www.blockchain.com/en/', 'https://www.blockchain.com/explorer/transactions/bch/{0}', 'https://www.blockchain.com/explorer/addresses/bch/{0}', 'https://www.blockchain.com/explorer/blocks/bch/{0}', 1),	


(2, 'https://www.blockcypher.com/', 'https://live.blockcypher.com/ltc/tx/{0}', 'https://live.blockcypher.com/ltc/address/{0}', 'https://live.blockcypher.com/ltc/block/{0}', 2),
(2, 'https://www.blockcypher.com/', 'https://live.blockcypher.com/doge/tx/{0}', 'https://live.blockcypher.com/doge/address/{0}', 'https://live.blockcypher.com/doge/block/{0}', 2),
(2, 'https://www.blockcypher.com/', 'https://live.blockcypher.com/dash/tx/{0}', 'https://live.blockcypher.com/dash/address/{0}', 'https://live.blockcypher.com/dash/block/{0}', 2),


(3, 'https://binance.mintscan.io/', 'https://binance.mintscan.io/txs/{0}', 'https://binance.mintscan.io/account/{0}', 'https://www.mintscan.io/blocks/{0}', 3),
(3, 'https://binance.mintscan.io/', 'https://binance.mintscan.io/cosmos/txs/{0}', 'https://binance.mintscan.io/cosmos/account/{0}', 'https://www.mintscan.io/cosmos/blocks/{0}', 3),
(3, 'https://binance.mintscan.io/', 'https://binance.mintscan.io/quasar/txs/{0}', 'https://binance.mintscan.io/quasar/account/{0}', 'https://www.mintscan.io/quasar/blocks/{0}', 3),

(4, 'https://bscscan.com/', 'https://bscscan.com/tx/{0}', 'https://bscscan.com/address/{0}', 'https://bscscan.com/token/{1}?a={0}', 'https://bscscan.com/block/{0}', 4),

(5, 'https://etherscan.io/', 'https://etherscan.io/tx/{0}', 'https://etherscan.io/address/{0}', 'https://etherscan.io/token/{1}?a={0}', 'https://etherscan.io/block/{0}', 6),

(6, 'https://bitinfocharts.com/', 'https://bitinfocharts.com/bitcoin/tx/{0}', 'https://bitinfocharts.com/bitcoin/address/{0}', 'https://bitinfocharts.com/en/bitcoin/block/{0}', 4),
(6, 'https://bitinfocharts.com/', 'https://bitinfocharts.com/litecoin/tx/{0}', 'https://bitinfocharts.com/litecoin/address/{0}', 'https://bitinfocharts.com/litecoin/block/{0}', 4),
(6, 'https://bitinfocharts.com/', 'https://bitinfocharts.com/dogecoin/tx/{0}', 'https://bitinfocharts.com/dogecoin/address/{0}', 'https://bitinfocharts.com/dogecoin/block/{0}', 4),

(7, 'https://blockchair.com/', 'https://blockchair.com/bitcoin/transaction/{0}', 'https://blockchair.com/bitcoin/address/{0}', 'https://blockchair.com/bitcoin/block/{0}', 5),
(7, 'https://blockchair.com/', 'https://blockchair.com/ethereum/transaction/{0}', 'https://blockchair.com/ethereum/address/{0}', 'https://blockchair.com/ethereum/block/{0}', 5),

(8, 'https://blockexplorer.one/', 'https://blockexplorer.one/bitcoin/mainnet/tx/{0}', 'https://blockexplorer.one/bitcoin/mainnet/address/{0}', 'https://blockexplorer.one/bitcoin/mainnet/blockHash/{0}', 7),
(8, 'https://blockexplorer.one/', 'https://blockexplorer.one/litecoin/mainnet/tx/{0}', 'https://blockexplorer.one/litecoin/mainnet/address/{0}', 'https://blockexplorer.one/litecoin/mainnet/blockHash/{0}', 7),
(8, 'https://blockexplorer.one/', 'https://blockexplorer.one/ethereum/mainnet/tx/{0}', 'https://blockexplorer.one/ethereum/mainnet/address/{0}', 'https://blockexplorer.one/ethereum/mainnet/blockHash/{0}', 7),

(9, 'https://chainz.cryptoid.info/', 'https://btc.cryptoid.info/btc/tx.dws?{0}.htm', 'https://btc.cryptoid.info/btc/address.dws?{0}.htm', 'https://btc.cryptoid.info/btc/block.dws?{0}.htm', 9),
(9, 'https://chainz.cryptoid.info/', 'https://btc.cryptoid.info/ltc/tx.dws?{0}.htm', 'https://btc.cryptoid.info/ltc/address.dws?{0}.htm', 'https://chainz.cryptoid.info/ltc/block.dws?{0}.htm', 9),
(9, 'https://chainz.cryptoid.info/', 'https://btc.cryptoid.info/ion/tx.dws?{0}.htm', 'https://btc.cryptoid.info/ion/address.dws?{0}.htm', 'https://chainz.cryptoid.info/ion/block.dws?{0}.htm', 9),

(10, 'https://dashblockexplorer.com/', 'https://dashblockexplorer.com/tx/{0}', 'https://dashblockexplorer.com/address/{0}', 'https://dashblockexplorer.com/block/{0}', 8),

(11, 'https://dogechain.info/', 'https://dogechain.info/tx/{0}', 'https://dogechain.info/address/{0}', 'https://dogechain.info/block/{0}', 10),

(12, 'https://beaconcha.in/', 'https://beaconcha.in/tx/{0}', 'https://beaconcha.in/address/{0}', 'https://beaconcha.in/block/{0}', 11),

(14, 'https://ethplorer.io/', 'https://etherscan.io/tx/{0}', 'https://etherscan.io/address/{0}', 'https://etherscan.io/block/{0}', 13),

(15, 'https://polygonscan.com/', 'https://polygonscan.com/{0}', 'https://polygonscan.com/address/{0}', 'https://etherscan.io/token/{1}?a={0}', 'https://polygonscan.com/block/{0}', 14),

(16, 'https://tronscan.org/#/', 'https://tronscan.org/#/transaction/{0}', 'https://tronscan.org/#/address/{0}', 'https://tronscan.org/#/block/{0}', 15),

