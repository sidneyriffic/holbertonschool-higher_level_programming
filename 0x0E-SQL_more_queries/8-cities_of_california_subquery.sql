-- select all cities in california by getting id from second table
-- select all cities in california by getting id from second table
SELECT * FROM cities WHERE state_id=(SELECT id FROM states
WHERE name="California")
