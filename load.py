from config import DB_URL
from sqlalchemy import create_engine
import pandas as pd

def load_data(data):
    engine = create_engine(DB_URL)
    df = pd.DataFrame(data)

    df.to_sql(
        "products",
        engine,
        if_exists="append",
        index=False
    )