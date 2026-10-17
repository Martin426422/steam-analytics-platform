use SteamAnalytics
CREATE TABLE users
(
    user_id INT IDENTITY(1,1) PRIMARY KEY,

    username VARCHAR(100) NOT NULL UNIQUE,

    email VARCHAR(255) NOT NULL UNIQUE,

    password_hash VARCHAR(255) NOT NULL,

    created_at DATETIME DEFAULT GETDATE()
);