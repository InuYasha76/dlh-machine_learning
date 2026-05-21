-- Creates stored procedure AddBonus that adds a new correction for a student.
-- If the project doesn't exist, inserts it into the projects table.


DELIMITER //

CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT
)
BEGIN
	DECLARE project_id INT;

	-- Retrieve the id of the project by name, NULL if not found
	SELECT id INTO project_id
	FROM projects
	WHERE name = project_name;

	-- Insert project if not exists
	IF project_id IS NULL THEN
		INSERT INTO projects (name)
		VALUES (project_name);

		-- Retrieves the last inserted project id
		SET project_id = LAST_INSERT_ID();
	END IF;

	-- Inserts a correction 
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, project_id, score);
END //

DELIMITER ;
