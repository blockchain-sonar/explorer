CREATE SEQUENCE "explorer_id_seq" START 1;

CREATE TABLE "explorer" (
    "id"        BIGINT PRIMARY KEY      NOT NULL,
    "explorer"  CHARACTER VARYING(100)  NOT NULL
);