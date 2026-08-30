use SteamAnalytics

CREATE TABLE games
(
    appid INT PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    developer NVARCHAR(255) NOT NULL,
    publisher NVARCHAR(255) NOT NULL
)

CREATE TABLE game_stats
(
    stat_id INT IDENTITY(1,1) PRIMARY KEY,

    appid INT NOT NULL,

    snapshot_date DATE NOT NULL,

    positive INT,
    negative INT,

    avg_playtime_forever INT,
    avg_playtime_2weeks INT,

    median_playtime_forever INT,
    median_playtime_2weeks INT,

    price_usd DECIMAL(10,2),
    initial_price_usd DECIMAL(10,2),

    discount INT,
    ccu INT,

    owners_min BIGINT,
    owners_max BIGINT,

    positive_review_pct DECIMAL(5,2),

    CONSTRAINT FK_game_stats_games
        FOREIGN KEY (appid)
        REFERENCES games(appid)
)

go