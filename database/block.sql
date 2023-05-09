CREATE SEQUENCE "block_id_seq" START 1;

CREATE TABLE "block" (
    "id"            BIGINT PRIMARY KEY  NOT NULL    DEFAULT NEXTVAL('blockchain_id_seq'),
    "number"        BIGINT              NOT NULL,
    "hash"          BYTEA               NOT NULL,
    "parent_hash"   BYTEA               NOT NULL,
    "blockchain_id" BIGINT              NOT NULL,
    CONSTRAINT "fk__block__blockchain" FOREIGN KEY ("blockchain_id") REFERENCES "blockchain" ("id")
);

-- ALTER TABLE "block" ALTER COLUMN "id" SET DEFAULT NEXTVAL('block_id_seq');

-- INSERT INTO public.block(
-- 	"number", hash, parent_hash, blockchain_id)
-- 	VALUES (567789, ('\x00000000030a4e13565e8e89e26f838c62816460fb2b3f76b8f654aa802e37ce'::bytea), ('\x00000000030a4e12ad81558fbc78f10e1c38c7c64114e83150438c029c820424'::bytea), 1);