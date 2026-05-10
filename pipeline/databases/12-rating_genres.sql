-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Results must be displayed as name, rating.
-- Results must be sorted in descending order by rating
SELECT 
    tg.name AS name, 
    SUM(tsr.rate) AS rating
FROM tv_genres tg
INNER JOIN tv_show_genres tsg 
    ON tg.id = tsg.genre_id
INNER JOIN tv_show_ratings tsr
	ON tsg.show_id = tsr.show_id
GROUP BY name
ORDER BY rating DESC;
