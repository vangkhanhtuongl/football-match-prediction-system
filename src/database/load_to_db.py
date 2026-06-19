from src.database.db_connection import get_engine

def load_to_postgres(df, table_name):

    engine = get_engine()

    try:
        df.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False,
            method="multi",
            chunksize=5000
        )

        print(f"SUCCESS: Loaded {len(df)} rows into {table_name}")

    except Exception as e:

        print("\n" + "=" * 60)
        print(f"TABLE: {table_name}")
        print(f"ERROR TYPE: {type(e).__name__}")

        if hasattr(e, "orig"):
            print("\nPOSTGRES ERROR:")
            print(e.orig)

        print("=" * 60 + "\n")

        raise