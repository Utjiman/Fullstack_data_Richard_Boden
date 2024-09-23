SELECT * FROM chess;

DESCRIBE chess_db.main.chess;

-- chess games ex 0.b)
SELECT DISTINCT winner FROM chess_db.main.chess;

-- chess games ex 0.c)
SELECT DISTINCT victory_status FROM chess_db.main.chess;

-- chess games ex 0.d) returnerar totala antalet rader i tabellen
SELECT COUNT(*) AS total_games
FROM chess_db.main.chess;

-- chess game ex 0.e)
 SELECT "winner", COUNT(*) FROM chess_db.main.chess group by winner; 

-- chess game ex 0.f)
SELECT
	"opening_ply",
	COUNT(*) as most_played_start
FROM
	chess_db.main.chess
group by
	opening_ply
ORDER BY
	most_played_start DESC
LIMIT 10;

-- chess game ex 0.g)
-- GREATEST(white_rating, black_rating): Jämför värdena för vit- och svartspelarens rating och returnerar det högsta.
-- CASE: Används för att välja spelaren (antingen vit eller svart) med den högsta rankingen.
-- ORDER BY highest_rating DESC: Sorterar resultaten i fallande ordning baserat på ratingen.
-- LIMIT 1: Begränsar resultatet till endast det högsta värdet.
-- Detta ger dig spelaren med den högsta rankingen och deras rating.

SELECT 
    CASE 
        WHEN white_rating > black_rating THEN white_id
        ELSE black_id
    END AS highest_rated_player,
    GREATEST(white_rating, black_rating) AS highest_rating
FROM chess_db.main.chess
ORDER BY highest_rating DESC
LIMIT 5;



