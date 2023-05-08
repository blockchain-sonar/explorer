CREATE TABLE block (
    id BIGINT PRIMARY KEY,
    number_id BIGINT,
    hash BYTEA,
    parent_hash BYTEA
);