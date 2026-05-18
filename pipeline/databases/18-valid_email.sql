-- Creates a trigger that resets valid_email when email changes.
DELIMITER //

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
		SET valid_email = 0;
END //

DELIMITER ;
