USE SteamAnalytics
GO
CREATE VIEW vw_gold_game_performance AS
SELECT
    g.appid,
    g.name,
    g.publisher,
    g.developer,
    gs.snapshot_date,
    gs.price_usd,
    gs.discount,
    gs.owners_min,
    gs.owners_max,
    (gs.owners_min + gs.owners_max) / 2.0 AS estimated_owners,
    gs.positive_review_pct,
    gs.ccu,
    gs.avg_playtime_forever
FROM games g
JOIN game_stats gs
    ON g.appid = gs.appid;
GO

CREATE VIEW vw_gold_publisher_stats
AS
SELECT
    g.publisher,
    COUNT(*) AS game_count,
    AVG(gs.positive_review_pct) AS avg_rating,
    AVG(gs.price_usd) AS avg_price,
    SUM((gs.owners_min + gs.owners_max) / 2.0) AS estimated_owners
FROM games g
JOIN game_stats gs
    ON g.appid = gs.appid
GROUP BY g.publisher;
GO

CREATE VIEW vw_gold_top_games
AS
SELECT
    g.name,
    (gs.owners_min + gs.owners_max) / 2.0 AS estimated_owners,
    gs.positive_review_pct,
    gs.price_usd,
    gs.ccu
FROM games g
JOIN game_stats gs
    ON g.appid = gs.appid;
GO