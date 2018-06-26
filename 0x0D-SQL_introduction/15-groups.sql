-- return count of each score
-- return count of each score
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score ORDER BY COUNT(score) DESC
