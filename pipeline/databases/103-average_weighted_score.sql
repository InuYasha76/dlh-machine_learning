-- Creates a stored procedure that computes and stores the average weighted score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN input_user_id INT)
BEGIN
    UPDATE users u
    LEFT JOIN (
        SELECT 
            cor.user_id,
            SUM(cor.score * p.weight) / SUM(p.weight) AS weighted_avg_score
        FROM corrections cor
        INNER JOIN projects p ON cor.project_id = p.id
        WHERE cor.user_id = input_user_id
        GROUP BY cor.user_id
    ) c ON c.user_id = u.id
    SET u.average_score = COALESCE(c.weighted_avg_score, 0)
    WHERE u.id = input_user_id;
END //

DELIMITER ;
