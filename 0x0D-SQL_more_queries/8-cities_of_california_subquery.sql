-- all cities in California
-- all cities
SELECT id, name
FROM cities
WHERE state_id in (
      SELECT id
      FROM states
      WHERE name = 'California'
      )
ORDER BY cities.id ASC;
