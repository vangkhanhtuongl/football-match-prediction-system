import pandas as pd


def strip_strings(df):
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].astype(str).str.strip()

    return df


def remove_duplicates(df):
    return df.drop_duplicates()


def convert_dates(df, columns):
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

    return df


def convert_numeric(df, columns):
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    return df