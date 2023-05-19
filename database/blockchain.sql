CREATE SEQUENCE "blockchain_id_seq" START 1;

CREATE TABLE "blockchain" (
    "id"    BIGINT PRIMARY KEY      NOT NULL    DEFAULT NEXTVAL('blockchain_id_seq'),
    "name"  CHARACTER VARYING(100)  NOT NULL,
    -- "explorer_id"  BIGINT           NOT NULL,
    -- CONSTRAINT "fk__explorer__block" FOREIGN KEY ("explorer_id") REFERENCES "explorer" ("id")
);


-- INSERT INTO public.blockchain(
-- 	name)
-- 	VALUES ('Bitcoin'),
-- ('Litecoin'),
-- ('Ethereum'),
-- ('TRON'),
-- ('Solana'),
-- ('Cardano'),
-- ('Polygon');
