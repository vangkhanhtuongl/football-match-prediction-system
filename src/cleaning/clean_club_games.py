from src.cleaning.utils import load_csv, basic_clean
from src.database.load_to_db import load_to_postgres

df = load_csv("club_games.csv")

df = basic_clean(df)

df["is_win"] = df["is_win"].astype(bool)

df = df.dropna(
    subset=[
        "game_id",
        "club_id"
    ]
)

load_to_postgres(
    df,
    "club_games"
)



