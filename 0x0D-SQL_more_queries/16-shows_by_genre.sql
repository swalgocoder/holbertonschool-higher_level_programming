-- double right join, right on tv_show_genres, right on tv_show
-- NULL value  when show doesn't have a genre

SELECT tv_shows.title, tv_genres.name FROM tv_genres
RIGHT OUTER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
RIGHT OUTER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC;
