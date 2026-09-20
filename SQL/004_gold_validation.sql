USE SteamAnalytics;
-- duplicates
SELECT
    appid,
    COUNT(*) AS cnt
FROM games
GROUP BY appid
HAVING COUNT(*) > 1;

--game_stats rekords without games
SELECT *
FROM game_stats gs
LEFT JOIN games g
    ON gs.appid = g.appid
WHERE g.appid IS NULL;

-- count of games
SELECT COUNT(*) AS games_count
FROM games;

-- Count of statistics
SELECT COUNT(*) AS stats_count
FROM game_stats;

-- prices range
SELECT
    MIN(price_usd) AS min_price,
    MAX(price_usd) AS max_price
FROM game_stats;

-- review range
SELECT
    MIN(positive_review_pct) AS min_rating,
    MAX(positive_review_pct) AS max_rating
FROM game_stats;