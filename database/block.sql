CREATE SEQUENCE "block_id_seq" START 1;

CREATE TABLE "block" (
    "id"            BIGINT PRIMARY KEY  NOT NULL    DEFAULT NEXTVAL('block_id_seq'),
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

-- INSERT INTO public.block(
-- 	 "number", hash, parent_hash, blockchain_id)
-- 	VALUES (51090247, ('\x00000000030b934bce29e0d17d630fda98333daeafa24eb250f2ff06b484f244'::bytea), ('\x00000000030b934a61d20c4d88ab8414448a44f205db2d54e4a256c2fd3b4f0a'::bytea), 1),
-- (51090258, ('\x00000000030b93ff8628b8ed45ffe851d847401d91005c5ee46334a0717c2f2f'::bytea), ('\x00000000030b93fe787c1b89044acdb1ce7eb113b5d93cfb1101bc1644fb86c9'::bytea), 1),
-- (51090257, ('\x00000000030b949b63ed86e9409c03d55547298fca788cca5c927f99051834ee'::bytea), ('\x00000000030b949a41d3e50cb990f5af7a03951977faecbafc7803a21133441d'::bytea), 1),
-- (51090195, ('\x00000000030b94a32a799b9e4c7b6d5319a994f78857f51fe4cdab543ca120bb'::bytea), ('\x00000000030b94a20867d271c2e0552f2188298d4b3d849c4546a4e33ae845f5'::bytea), 1),
-- (789384, ('\x00000000000000000001ff4178367363678156ce86d7c4a8a5b35457bb1780df'::bytea), ('\x9a3147a6319f4f8592e9a9b3541dbfd318af34a8a6441d59ac7e549c74e607ad'::bytea), 2),
-- (789373, ('\x00000000000000000000343505c376a3913da102c0bf3df22b42d573e2cb2e64'::bytea), ('\x201e77e86a962bb6b532b9e398a7e1f2047bff1fa87f1f5e6ffd5eb1576feb9f'::bytea), 2);