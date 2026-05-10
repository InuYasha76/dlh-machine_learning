-- Creates a table called first_table in the current database
-- id: INT
-- name: VARCHAR(256)
-- Does not fail if the table already exists
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
