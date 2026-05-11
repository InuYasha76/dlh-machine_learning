-- Displays the max temperature of each state
-- Orders the display by State name (default order)
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
