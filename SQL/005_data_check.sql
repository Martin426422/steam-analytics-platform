use SteamAnalytics
SELECT COUNT(*) FROM games;

SELECT COUNT(*) FROM game_stats;

SELECT MAX(snapshot_date)
FROM game_stats;