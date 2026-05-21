-- Creates a function returning arg1/arg2, if arg2 is 0 or arg1 or arg2 are NULL, returns 0

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DOUBLE
DETERMINISTIC
BEGIN
	IF b = 0 OR a IS NULL OR b IS NULL THEN
		RETURN 0;
	END IF;
	RETURN ROUND(CAST(a AS DOUBLE) / b, 6);
END //

DELIMITER ;



