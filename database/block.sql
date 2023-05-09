CREATE SEQUENCE "block_id_seq" START 1;

CREATE TABLE "block" (
    "id"            BIGINT PRIMARY KEY  NOT NULL DEFAULT NEXTVAL('blockchain_id_seq'),
    "number"        BIGINT              NOT NULL,
    "hash"          BYTEA               NOT NULL,
    "parent_hash"   BYTEA               NOT NULL,
    "blockchain_id" BIGINT              NOT NULL,
    CONSTRAINT "fk__block__blockchain" FOREIGN KEY ("blockchain_id") REFERENCES "blockchain" ("id")
);

-- ALTER TABLE "block" ALTER COLUMN "id" SET DEFAULT NEXTVAL('block_id_seq');