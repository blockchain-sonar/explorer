CREATE SEQUENCE "address_id_seq" START 1;

CREATE TABLE "address" (
    "id"        BIGINT PRIMARY KEY  NOT NULL    DEFAULT NEXTVAL('address_id_seq'),
    "address"   BYTEA               NOT NULL,
    "balance"   NUMERIC(48,24)
);
