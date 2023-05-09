CREATE TABLE "address" (
    "id"        BIGINT PRIMARY KEY  NOT NULL,
    "address"   BYTEA               NOT NULL,
    "balance"   NUMERIC(48,24)
);
