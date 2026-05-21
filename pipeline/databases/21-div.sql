-- Creates a function returning arg1/arg2, if arg2 is 0 or arg1 or arg2 are NULL, returns 0

DELIMITER //

CREATE FUNCTION SafeDiv(arg1 INT, arg2 INT)
RETURNS DOUBLE
DETERMINISTIC
BEGIN
	IF arg2 = 0 OR arg1 IS NULL OR arg2 IS NULL THEN
		RETURN 0;
	END IF;
	RETURN ROUND(arg1 / arg2, 6);
END //

DELIMITER ;



