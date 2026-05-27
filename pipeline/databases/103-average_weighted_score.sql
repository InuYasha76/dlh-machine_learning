-- Creates a stored procedure that computes and store the average weighted score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users u
    LEFT JOIN (
        SELECT
			cor.user_id,
			SUM(cor.score * p.weight) / SUM(p.weight) AS weighted_avg_score
        FROM corrections cor
		INNER JOIN projects p ON cor.project_id = p.id
        WHERE cor.user_id = ComputeAverageScoreForUser.user_id
        GROUP BY cor.user_id
    ) c ON c.user_id = u.id
    SET u.average_score = c.weighted_avg_score;
END //

DELIMITER ;
