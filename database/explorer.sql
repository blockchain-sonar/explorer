CREATE SEQUENCE "explorer_id_seq" START 1;
CREATE TABLE "explorer" (
    "id" BIGINT PRIMARY KEY NOT NULL DEFAULT NEXTVAL('explorer_id_seq'),
    "name" CHARACTER VARYING(100) NOT NULL
);
INSERT INTO public.explorer(name)
VALUES  ('Blockchain'),
        ('Blockcypher'),
        ('BinancemintscanExplorer'),
        ('BitqueryExplorer'),
        ('BscscanExplorer'),
        ('EtherscanExplorer'),
        ('BitinfochartsExplorer'),
        ('BlockchairExplorer'),
        ('BlockexplorerExplorer'),
        ('BtcExplorer'),
        ('ChainzcryptoidExplorer'),
        ('DashblockExplorer'),
        ('DogechainExplorer'),
        ('EtherchainExplorer'),
        ('EtherscanExplorer'),
        ('EthplorerExplorer'),
        ('LitecoinblockExplorer'),
        ('PolygonscanExplorer'),
        ('TronscanExplorer'),



  