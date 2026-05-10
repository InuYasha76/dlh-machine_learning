-- lists all shows from hbtn_0d_tvshows_rate by their rating
-- Results must be displayed as title, rating
-- Results must be sorted in descending order by the rating
SELECT 
    ts.title AS title, 
    SUM(tsr.rate) AS rating
FROM tv_shows ts
INNER JOIN tv_show_ratings tsr 
    ON ts.id = tsr.show_id
GROUP BY ts.title
ORDER BY rating DESC;
