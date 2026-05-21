-- Creates stored procedure AddBonus that adds a new correction for a student.

DELIMITER //

CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT
)
BEGIN
	DECLARE project_id INT;

	-- Insert if not exists, else execute ON DUPLICATE KEY
	INSERT INTO projects (name)
	VALUES (project_name)
	ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id);
	
	-- Retrieve id of existing or inserted row that's stored in the session
	SET project_id = LAST_INSERT_ID();

	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, project_id, score);
END //

DELIMITER ;
