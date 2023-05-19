CREATE SEQUENCE "transaction_id_seq" START 1;

CREATE TABLE "transaction" (
    "id"          BIGINT PRIMARY KEY  NOT NULL    DEFAULT NEXTVAL('transaction_id_seq'),
    "hash"        BYTEA               NOT NULL,
    "amount"      NUMERIC(48,24),
    "block_id"    BIGINT              NOT NULL,
    CONSTRAINT "fk__transaction__block" FOREIGN KEY ("block_id") REFERENCES "block" ("id")
);

-- INSERT INTO public.transaction(
-- 	hash, amount, block_id)
-- 	VALUES ('c13b2c9e1047cebc381d82a94b90a97853d0f0c711f83f2506697067a7245522'::bytea, 0.0000023, 1),
-- 	('821d9d3394dd21ea1172f7772d7738f0a7b48f23bfe73a2966fe1eda57a677f3'::bytea, 0.000001, 2),
-- ('192b3ea24c63ed527d962ae92d699c70ead06c0d90265bb86db30177849c81f1'::bytea, 6264.29, 4),
-- ('d82fd5e6e25efd0a48f5115fa0161ca95647e8c2cde3375f9f03e9297974f557'::bytea, 32011.48, 5),
-- ('e494244c1e7f7357928284661f1c780ca301e2a5d24ec1b09409c98fcd28465e'::bytea, 88.888888, 3);