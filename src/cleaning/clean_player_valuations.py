from src.cleaning.utils import load_csv, basic_clean
from src.database.load_to_db import load_to_postgres

df = load_csv("player_valuations.csv")

df = basic_clean(df)

load_to_postgres(
    df,
    "player_valuations"
)