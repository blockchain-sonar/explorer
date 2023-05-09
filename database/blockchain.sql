CREATE SEQUENCE "blockchain_id_seq" START 1;

CREATE TABLE "blockchain" (
    "id"    BIGINT PRIMARY KEY      NOT NULL    DEFAULT NEXTVAL('blockchain_id_seq'),
    "name"  CHARACTER VARYING(100)  NOT NULL
);

