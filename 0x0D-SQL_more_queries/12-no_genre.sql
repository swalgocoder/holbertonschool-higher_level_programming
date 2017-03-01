-- all shows in hbtn_0d.tvshows without a genre match
-- left outer join, all id data from tv_shows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
