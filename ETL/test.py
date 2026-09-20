from sqlalchemy import create_engine, text

engine = create_engine(
    "mssql+pyodbc://Martin\\SQLEXPRESS/SteamAnalytics"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

with engine.begin() as conn:
    conn.execute(text("""
        INSERT INTO games
        (appid, name, developer, publisher)
        VALUES
        (:appid, :name, :developer, :publisher)
    """), {
        "appid": 99999999,
        "name": "鬼谷八荒 Tale of Immortal",
        "developer": "鬼谷工作室",
        "publisher": "鬼谷工作室"
    })