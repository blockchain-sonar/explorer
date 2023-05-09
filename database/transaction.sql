CREATE SEQUENCE "transaction_id_seq" START 1;

CREATE TABLE "transaction" (
    "id"        BIGINT PRIMARY KEY  NOT NULL    DEFAULT NEXTVAL('transaction_id_seq'),
    "hash"      BYTEA               NOT NULL,
    "amount"    NUMERIC(48,24),
    "block_id" BIGINT               NOT NULL,
    CONSTRAINT "fk__transaction__block" FOREIGN KEY ("block_id") REFERENCES "block" ("id")
);