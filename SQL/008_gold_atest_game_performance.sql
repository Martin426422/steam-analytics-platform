CREATE VIEW vw_gold_latest_game_performance
AS
WITH latest_snapshot AS
(
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY appid
            ORDER BY snapshot_date DESC
        ) AS rn
    FROM game_stats
)
SELECT
    g.appid,
    g.name,
    g.publisher,
    g.developer,
    ls.snapshot_date,
    ls.price_usd,
    ls.discount,
    ls.ccu,
    ls.estimated_owners,
    ls.positive_review_pct,
    ls.avg_playtime_forever
FROM latest_snapshot ls
JOIN games g
    ON g.appid = ls.appid
WHERE rn = 1;
GO