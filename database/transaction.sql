CREATE TABLE transaction (
    id BIGINT PRIMARY KEY,
    hash BYTEA,
    amount NUMERIC(48,24)
);