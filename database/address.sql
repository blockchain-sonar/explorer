CREATE SEQUENCE "address_id_seq" START 1;

CREATE TABLE "address" (
    "id"                BIGINT PRIMARY KEY  NOT NULL    DEFAULT NEXTVAL('address_id_seq'),
    "address"           BYTEA               NOT NULL,
    "balance"           NUMERIC(48,24),
    "transaction_id"    BIGINT              NOT NULL,
    CONSTRAINT "fk__address__block" FOREIGN KEY ("transaction_id") REFERENCES "transaction" ("id")
);


-- INSERT INTO public.address(
-- 	address, balance, transaction_id)
-- 	VALUES (('TYL7z7VSVRShLoJ6YRQMA4t9pSECt9ZLtr'::bytea), 997224171.14, 12),
-- (('TLbkcH7QLcULY8dpPAbD9EYGLUWKbeRxuB'::bytea), 997224171.15, 13),
-- (('TFKSWmnRJkzCfWUr56DQ1zqGCxZLW9dKSv'::bytea), 997224171.16, 14),
-- (('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5'::bytea), 0.01847823, 15),
-- (('3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZd8'::bytea), 0.01847824, 13);