CREATE TABLE "transaction" (
    "id"        BIGINT PRIMARY KEY  NOT NULL,
    "hash"      BYTEA               NOT NULL,
    "amount"    NUMERIC(48,24)
);