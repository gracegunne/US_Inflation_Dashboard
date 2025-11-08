import os, requests, pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
FRED_KEY = os.getenv("FRED_API_KEY")
BASE = "https://api.stlouisfed.org/fred/series/observations"
SERIES = ["CPIAUCSL","CPILFESL","PCEPI","T5YIE","FEDFUNDS","USREC"]

def _ensure_dir(path: str):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)

def fetch_series(series_id: str, start="1980-01-01") -> pd.Series:
    params = {"series_id": series_id, "api_key": FRED_KEY, "file_type": "json", "observation_start": start}
    r = requests.get(BASE, params=params, timeout=30)
    r.raise_for_status()
    obs = r.json()["observations"]
    s = pd.Series({
        pd.Period(o["date"][:10], freq="M").to_timestamp("M"): float(o["value"]) if o["value"] not in (".", "") else None
        for o in obs
    }, name=series_id)
    return s.sort_index()

def load_fred_cache(path="data/cache_fred.csv", max_age_days=1) -> pd.DataFrame:
    _ensure_dir(path)
    if os.path.exists(path):
        mtime = datetime.fromtimestamp(os.path.getmtime(path))
        if datetime.now() - mtime < timedelta(days=max_age_days):
            return pd.read_csv(path, parse_dates=["date"]).set_index("date")
    if not FRED_KEY:
        raise RuntimeError("Missing FRED_API_KEY. Add it to a .env file.")
    df = pd.concat([fetch_series(s) for s in SERIES], axis=1)
    df.to_csv(path, index_label="date")
    return df
