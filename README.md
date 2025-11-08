# US Inflation Panel (Dash)

My panel for the 4-panel group dashboard. It shows US inflation (CPI, Core CPI, PCE) with YoY / MoM / SAAR, a 2% guide, recession shading, and an optional Fed funds overlay.

## Run locally
1) `pip install -r requirements.txt`
2) Create `.env`:FRED_API_KEY=1dd02e9ef189ec207cf5b5a5ab762be6
3) `python app.py` → open the link in the terminal.

## Run inside a notebook (no browser tab)
- Open `notebook.ipynb` and run the first cell (uses JupyterDash).

## Data & transforms
- FRED: `CPIAUCSL`, `CPILFESL`, `PCEPI`, `T5YIE`, `FEDFUNDS`, `USREC`
- Computed: YoY %, MoM %, MoM SAAR, optional 3-month smoothing
- Data cached to `data/cache_fred.csv` for speed.

## Notes
- YoY for trend, MoM/SAAR for near-term momentum.
- First 12 months are NaN for YoY by construction.

