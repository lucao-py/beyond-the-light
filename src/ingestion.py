import pandas as pd
from pathlib import Path

URL = (
    "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
    "?query=select+*+from+cumulative&format=csv"
)

path = Path("data/raw/kepler_cumulative.csv")

if not path.exists():
    df = pd.read_csv(URL)
    Path("data/raw/").mkdir(parents=True, exist_ok=True)
    df.to_csv("data/raw/kepler_cumulative.csv", index = False)

    print(f"linhas: {df.shape[0]} | colunas: {df.shape[1]}")
else:
    print(f"arquivo já existe, nada foi baixado.")





