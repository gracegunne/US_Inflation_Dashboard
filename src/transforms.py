import pandas as pd

def yoy(series: pd.Series) -> pd.Series:
    return series.pct_change(12) * 100

def mom(series: pd.Series) -> pd.Series:
    return series.pct_change(1) * 100

def saar(series: pd.Series) -> pd.Series:
    m = mom(series) / 100.0
    return ((1 + m) ** 12 - 1) * 100

def normalize_100(series: pd.Series) -> pd.Series:
    base = series.iloc[0]
    return (series / base) * 100 if pd.notna(base) else series

def roll3(series: pd.Series) -> pd.Series:
    return series.rolling(3).mean()
