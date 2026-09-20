SELECT TOP 10
    g.name,
    gs.owners_max
FROM game_stats gs
JOIN games g
    ON gs.appid = g.appid
ORDER BY gs.owners_max DESC;

SELECT TOP 10
    g.name,
    gs.positive_review_pct
FROM game_stats gs
JOIN games g
    ON gs.appid = g.appid
WHERE gs.positive_review_pct > 0
ORDER BY gs.positive_review_pct DESC;

SELECT TOP 10
    g.name,
    gs.price_usd
FROM game_stats gs
JOIN games g
    ON gs.appid = g.appid
ORDER BY gs.price_usd DESC;

SELECT
    AVG(price_usd) AS avg_price
FROM game_stats;