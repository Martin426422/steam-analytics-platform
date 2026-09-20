use SteamAnalytics
ALTER TABLE game_stats
ADD CONSTRAINT UQ_game_snapshot
UNIQUE(appid, snapshot_date);
go