-- display average temperatures grouped by city
-- display average temperatures grouped by city
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC
