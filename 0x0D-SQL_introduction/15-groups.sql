-- return count of each score
-- return count of each score
SELECT score, COUNT(score) FROM second_table
GROUP BY score ORDER BY COUNT(score) DESC
