-- Creates a trigger that resets valid_email when email changes.
DELIMITER //

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email AND OLD.valid_email = NEW.valid_email THEN
		SET NEW.valid_email = 0;
	END IF;
END //

DELIMITER ;
