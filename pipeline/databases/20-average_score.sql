-- Create a stored procedure that computes & stores a student's average score
-- Args: user_id, a user_id

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users u
	JOIN (
		SELECT user_id, avg(score) AS average_score
		FROM corrections cor
		WHERE cor.user_id = user_id
		GROUP BY user_id
	) c ON c.user_id = u.id
	SET u.average_score = c.average_score;
END //

DELIMITER ;
