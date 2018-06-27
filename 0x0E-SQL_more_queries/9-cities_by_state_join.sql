-- select all cities and display state information using join
-- select all cities and display state information using join
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states
ON cities.state_id=states.id;
