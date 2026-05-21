-- Creates a function returning arg1/arg2, if arg2 is 0 or arg1 or arg2 are NULL, returns 0

DELIMITER //

CREATE FUNCTION SafeDiv(
	IN arg1 DOUBLE,
	IN arg2 DOUBLE
)
RETURNS DOUBLE
DETERMINISTIC
BEGIN
	IF arg2 = 0 OR IS NULL arg1 OR IS NULL arg2 THEN
		RETURN 0;
	END IF;
	RETURN arg1 / arg2;
END //

DELIMITER ;



