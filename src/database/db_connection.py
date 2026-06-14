from sqlalchemy import create_engine
from sqlalchemy import text


DB_USER = "postgres"
DB_PASSWORD = "ongchancon"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "football_prediction"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("Connected successfully!")
        print(result.fetchone())

except Exception as e:
    print("Connection failed!")
    print(e)

def get_engine():
    return engine