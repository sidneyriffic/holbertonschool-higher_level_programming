-- show all genres for the show "Dexter"
SELECT tv_genres.name AS name FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
AND tv_shows.title="Dexter"
RIGHT JOIN tv_genres ON tv_show_genres.genre_id=tv_genres.id
WHERE genre_id IS NULL ORDER BY name
