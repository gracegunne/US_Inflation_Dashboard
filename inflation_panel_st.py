
import os, pathlib, time
from typing import Dict, List

import numpy as np
import pandas as pd
import requests
from dotenv import load_dotenv

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- Config ----------------
APP_TITLE = "US Inflation (5Y) — Matplotlib/Seaborn"
CACHE_DIR = pathlib.Path("data"); CACHE_DIR.mkdir(parents=True, exist_ok=True)
CACHE_PATH = CACHE_DIR / "cache_fred.csv"
CACHE_MAX_AGE_HOURS = 24

SERIES_META = {
    "CPIAUCSL": {"name": "CPI (Headline)"},
    "CPILFESL": {"name": "CPI (Core ex F&E)"},
    "PCEPI":    {"name": "PCE Price Index"},
    "FEDFUNDS": {"name": "Fed Funds"},
    "USREC":    {"name": "NBER Recession 0/1"},
}
PRICE_SERIES = ["CPIAUCSL", "CPILFESL", "PCEPI"]
USREC_SERIES = "USREC"
FRED_URL = "https://api.stlouisfed.org/fred/series/observations"

# --------------- Data utils ---------------
def _to_month_end(d):
    return (pd.to_datetime(d) + pd.offsets.MonthEnd(0))

def fetch_fred(series_id: str, api_key: str) -> pd.Series:
    params = {
        "series_id": series_id, "api_key": api_key, "file_type": "json",
        "frequency": "m", "aggregation_method": "eop", "observation_start": "1980-01-01"
    }
    r = requests.get(FRED_URL, params=params, timeout=30); r.raise_for_status()
    obs = r.json()["observations"]
    idx = pd.DatetimeIndex([_to_month_end(o["date"]) for o in obs], name="date")
    vals = [np.nan if o["value"] in (".","") else float(o["value"]) for o in obs]
    return pd.Series(vals, index=idx, name=series_id).resample("M").last()

def load_or_refresh_cache(api_key: str) -> pd.DataFrame:
    if CACHE_PATH.exists():
        age_h = (time.time() - CACHE_PATH.stat().st_mtime)/3600
        try:
            df = pd.read_csv(CACHE_PATH, parse_dates=["date"]).set_index("date").sort_index()
            if set(SERIES_META) <= set(df.columns) and age_h <= CACHE_MAX_AGE_HOURS:
                return df
        except Exception:
            pass
    frames = [fetch_fred(s, api_key) for s in SERIES_META.keys()]
    df = pd.concat(frames, axis=1).sort_index()
    df.to_csv(CACHE_PATH, index_label="date")
    return df

def last_n_years(df: pd.DataFrame, n=5) -> pd.DataFrame:
    cutoff = df.index.max() - pd.DateOffset(years=n)
    return df[df.index >= cutoff]

def compute_views(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    yoy = df[PRICE_SERIES].pct_change(12)*100
    mom = df[PRICE_SERIES].pct_change(1)*100
    saar = ((1 + mom/100.0)**12 - 1)*100
    idx = df[PRICE_SERIES].copy()
    return {"YoY": yoy, "MoM": mom, "SAAR": saar, "Index": idx}

def normalize_100(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for c in out.columns:
        s = out[c]
        start = s.loc[s.first_valid_index()] if s.first_valid_index() else np.nan
        if pd.notna(start) and start != 0:
            out[c] = s/start*100
    return out

def recession_blocks(usrec: pd.Series):
    rec = (usrec.fillna(0) > 0.5).astype(int)
    blocks, inblock, start = [], False, None
    for d, v in rec.items():
        if v and not inblock:
            inblock, start = True, d
        if not v and inblock:
            inblock = False; blocks.append((start, d))
    if inblock:
        blocks.append((start, rec.index[-1] + pd.offsets.MonthEnd(0)))
    return blocks

# --------------- App ----------------
st.set_page_config(APP_TITLE, layout="centered")
st.title(APP_TITLE)
st.caption("Always last 5 years. Data: FRED (CPIAUCSL, CPILFESL, PCEPI, FEDFUNDS, USREC).")

load_dotenv()
api_key = os.getenv("FRED_API_KEY", "")
if not api_key:
    st.error("Missing FRED_API_KEY in your .env (same folder).")
    st.stop()

wide = last_n_years(load_or_refresh_cache(api_key), 5)
views = compute_views(wide)

with st.sidebar:
    st.subheader("Controls")
    series = st.multiselect(
        "Series", options=PRICE_SERIES,
        format_func=lambda s: SERIES_META[s]["name"],
        default=["CPIAUCSL","CPILFESL"]
    )
    view = st.radio("View", ["YoY","MoM","SAAR","Index"], index=0, horizontal=False)
    smooth = st.checkbox("3-month smoothing", value=False)
    guide = st.checkbox("2% guide (YoY / Index start=100)", value=True)
    rec = st.checkbox("Recession shading", value=True)
    fed = st.checkbox("Fed Funds overlay (right axis)", value=False)

if not series:
    st.warning("Pick at least one series.")
    st.stop()

df = views[view].copy()
if view == "Index":
    df = normalize_100(df)
if smooth:
    df = df.rolling(3, min_periods=1).mean()

sns.set_theme()
fig, ax1 = plt.subplots(figsize=(9,5.2))
for sid in series:
    s = df[sid].dropna()
    if not s.empty:
        ax1.plot(s.index, s.values, label=SERIES_META[sid]["name"])

# Y-axis & guide
if view in ("YoY","MoM","SAAR"):
    ax1.set_ylabel("%")
    if guide and view == "YoY":
        ax1.axhline(2, linestyle="--")
else:
    ax1.set_ylabel("Index (Norm=100 @ start)")
    if guide:
        ax1.axhline(100, linestyle="--")

# Recessions
if rec:
    for a, b in recession_blocks(wide[USREC_SERIES]):
        ax1.axvspan(a, b, color="lightgray", alpha=0.25, lw=0)

# Fed Funds overlay
if fed:
    ff = wide["FEDFUNDS"].rolling(3, min_periods=1).mean()
    ax2 = ax1.twinx()
    ax2.plot(ff.index, ff.values, label="Fed Funds (rhs)")
    ax2.set_ylabel("%")
    ax2.grid(False)

ax1.set_xlabel("")
ax1.legend(loc="upper left", ncol=2)
ax1.grid(True, alpha=0.25)
st.pyplot(fig, clear_figure=True)

notes = []
if view == "SAAR": notes.append("SAAR = ((1 + MoM/100)^12 − 1) × 100.")
if smooth: notes.append("3-month moving average applied.")
if view == "Index": notes.append("Series normalized to 100 at start of 5-year window.")
st.caption(" ".join(notes))

