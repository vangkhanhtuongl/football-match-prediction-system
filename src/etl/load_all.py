import pandas as pd

from src.database.db_connection import get_engine 
engine = get_engine()

tables = {
    "competitions": "data/raw/competitions.csv",
    "clubs": "data/raw/clubs.csv",
    "players": "data/raw/players.csv",
    "games": "data/raw/games.csv",
    "appearances": "data/raw/appearances.csv",
    "game_events": "data/raw/game_events.csv",
    "player_valuations": "data/raw/player_valuations.csv",
    "club_games": "data/raw/club_games.csv",
    "transfers": "data/raw/transfers.csv"
}

for table_name, file_path in tables.items():

    print(f"Loading {table_name}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} rows")