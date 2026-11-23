import pandas as pd
from pathlib import Path

URL = (
    "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
    "?query=select+*+from+cumulative&format=csv"
)

df = pd.read_csv(URL)

print(f"tamanho do df {len(df)}, formato: {df.shape}")

path = Path("data/raw/kepler_cumulative.csv")

if not path.exists():
    Path("data/raw/").mkdir(parents=True, exist_ok=True)
    df.to_csv("data/raw/kepler_cumulative.csv", index = False)
else:
    print(f"arquivo já existe, nada foi baixado.")