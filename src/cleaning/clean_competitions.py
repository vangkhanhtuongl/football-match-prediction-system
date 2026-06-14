import pandas as pd

from src.cleaning.utils import *

df = pd.read_csv("data/raw/competitions.csv")

df = remove_duplicates(df)

df = strip_strings(df)

df = convert_numeric(
    df,
    ["country_id"]
)

df = df.dropna(
    subset=["competition_id"]
)

df.to_csv(
    "data/cleaned/competitions.csv",
    index=False
)