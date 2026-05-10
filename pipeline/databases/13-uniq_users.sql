-- creates a table users (
--		id, int, not null, auto-increment, pki
--		email, string 255, never null, unique
-- 		name string 255)
-- script should not fail if table already exists
-- make attribute unique directly in the table schema
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL,
	name VARCHAR(255),
	PRIMARY KEY (id),
	UNIQUE (email)
);
