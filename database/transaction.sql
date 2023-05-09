CREATE SEQUENCE "transaction_id_seq" START 1;

CREATE TABLE "transaction" (
    "id"        BIGINT PRIMARY KEY  NOT NULL    DEFAULT NEXTVAL('block_id_seq'),
    "hash"      BYTEA               NOT NULL,
    "amount"    NUMERIC(48,24),
    CONSTRAINT "fk__transaction__block" FOREIGN KEY ("block_id") REFERENCES "block" ("id")
);