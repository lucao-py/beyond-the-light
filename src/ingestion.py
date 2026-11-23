import pandas as pd

URL = (
    "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
    "?query=select+*+from+cumulative&format=csv"
)

df = pd.read_csv(URL)

print(f"tamanho do df {len(df)}, formato: {df.shape}")

df.to_csv("data/raw/kepler_cumulative.csv", index = False)