# US Inflation Dashboard<div align="center">



Quick way to visualize US inflation trends over the past 5 years using different CPI measures and the PCE index.<h1>US Inflation Dashboard (5Y)</h1>

<em>Interactive exploration of US inflation dynamics across 6 key inflation metrics with recession shading and Fed policy context.</em>

## What it does

</div>

Track 6 different inflation metrics (headline CPI, core CPI, PCE, energy, food, and housing) with options to view year-over-year, month-over-month, or annualized rates. Also shows Fed policy rate and recession periods for context.

## Overview

Data comes from FRED and gets cached for 24 hours so you're not constantly hitting their API.

This Streamlit app lets you explore US inflation across 6 comprehensive measures over a 5-year time horizon. You can quickly switch among CPI (headline, core, energy, food, housing) and PCE price index, view growth rates (YoY, MoM, SAAR) or level indices, apply smoothing, and overlay macro context (Fed Funds Rate, NBER recession periods, 2% guide line).

## Features

All data are pulled on demand from the Federal Reserve Economic Data (FRED) API and cached locally for 24 hours to minimize API calls.

- 6 inflation measures: CPI Headline, Core CPI (minus food & energy), PCE Price Index, CPI Energy, CPI Food, CPI Housing

- Shows last 5 years of data## Why it’s interesting

- View as YoY %, MoM %, annualized rate, or indexed to 100

- Line charts, bar charts, or bothThis dashboard makes it easy to answer practical macro questions:

- Optional 3-month smoothing- Are inflation trends accelerating or cooling right now (MoM vs SAAR)?

- Recession shading (NBER data)- How do different inflation components (energy, food, housing, core) compare?

- Fed Funds Rate overlay- Is inflation above/below the 2% guide line—and for how long?

- 2% guideline toggle- How does inflation typically move around recessions and policy tightening?



## Data Sources## Features



All data from FRED:* **6 comprehensive inflation metrics**: CPI Headline, CPI Core (ex Food & Energy), PCE Price Index, CPI Energy, CPI Food, CPI Housing

* Always displays last 5 years of data

- `CPIAUCSL` - Headline CPI* Multiple view transformations: YoY %, MoM %, annualized SAAR %, or Index (rebased to 100 at window start)

- `CPILFESL` - Core CPI (no food/energy)* Plot types: Lines, Bars, or hybrid Lines + Bars

- `PCEPI` - PCE Price Index (what the Fed actually watches)* Optional 3-month smoothing to reduce noise

- `CPIENGSL` - CPI Energy* Recession shading using NBER recession indicator (USREC)

- `CPIUFDSL` - CPI Food* Fed Funds Rate overlay with dual y‑axis

- `CPIHOSNS` - CPI Housing* 2% guide line (or 100 for index normalization) toggle

- `FEDFUNDS` - Fed Funds Rate* Lightweight, fast UI powered by Streamlit & Matplotlib/Seaborn

- `USREC` - Recession indicator

## Data Sources (FRED Series)

## Setup

| Purpose | Series ID | Description |

You need Python 3.9+ and a free FRED API key from https://fred.stlouisfed.org/|---------|-----------|-------------|

| Headline CPI | `CPIAUCSL` | Consumer Price Index for All Urban Consumers |

```bash| Core CPI | `CPILFESL` | CPI less Food & Energy |

git clone https://github.com/gracegunne/US_Inflation_Dashboard.git| PCE Price Index | `PCEPI` | Personal Consumption Expenditures Price Index (Fed's preferred measure) |

cd US_Inflation_Dashboard| CPI Energy | `CPIENGSL` | Energy component of CPI |

| CPI Food | `CPIUFDSL` | Food component of CPI |

# optional: virtual environment| CPI Housing | `CPIHOSNS` | Housing component of CPI |

python -m venv .venv| Policy Rate | `FEDFUNDS` | Effective Federal Funds Rate |

.venv\Scripts\Activate.ps1| Recession Indicator | `USREC` | NBER recession periods (0/1) |



pip install -r requirements.txt## Requirements



# add your FRED key* Python 3.9+ (tested with 3.11)

echo "FRED_API_KEY=YOUR_KEY_HERE" > .env* FRED API key (free from https://fred.stlouisfed.org/)

* Packages listed in `requirements.txt`

# run it

streamlit run inflation_panel_st.py## Quick Start

```

```bash

Open the local URL (usually http://localhost:8501).# Clone

git clone https://github.com/gracegunne/US_Inflation_Dashboard.git

## How to usecd US_Inflation_Dashboard



1. Pick an inflation metric from the dropdown# (Optional) create virtual environment (Windows PowerShell)

2. Choose how you want to view it (YoY, MoM, annualized, or index)python -m venv .venv

3. Turn on smoothing if the chart's too noisy\.venv\Scripts\Activate.ps1

4. Toggle recession shading, Fed rate, and 2% line as needed

# Install dependencies

The cache file (`data/cache_fred.csv`) saves data for 24 hours. Delete it if you need fresh data.pip install -r requirements.txt



## Troubleshooting# Create .env with your FRED key

echo "FRED_API_KEY=YOUR_KEY_HERE" > .env

**App asks for API key**: Either paste it in the sidebar or add it to a `.env` file

# Run the app

**Chart is empty**: Make sure you selected a seriesstreamlit run inflation_panel_st.py

```

**SAAR looks crazy**: Turn on smoothing

Then open the local URL Streamlit prints (usually http://localhost:8501).

**Data seems old**: Delete `data/cache_fred.csv` to refresh

### Screenshot

## What's included![Dashboard Preview](dashboard_screenshot.png)



```

inflation_panel_st.py   # main app## Configuration

data/cache_fred.csv     # cached data (auto-generated)

requirements.txt        # dependenciesCreate a `.env` file in the repository root containing:

README.md               # this file

``````

FRED_API_KEY=YOUR_FRED_KEY

## Ideas for later```



- Add more CPI components (transportation, medical, etc.)If the key is missing or invalid, the app now shows a sidebar prompt where you can paste a valid key without restarting. (For persistent use still add it to `.env`.)

- Export charts directly

- Compare to Fed projections### Caching

- Show cache ageDownloaded observations are saved in `data/cache_fred.csv` and reused for up to 24 hours. Delete the file (or change system time range significantly) to force a refresh.

- Custom date ranges

## Usage Guide

---

1. Select the inflation series you want from the dropdown in the sidebar (choose from 6 inflation metrics).

Data from Federal Reserve Bank of St. Louis (FRED). Built with Streamlit and the usual Python data stack.2. Choose the view (YoY, MoM, SAAR, Index). Index will rebase chosen series to 100 at the start of the 5-year window.

3. Optionally enable 3-month smoothing to reduce noise.
4. Change plot style (lines, bars, combo) depending on preference.
5. Toggle recession shading, Fed Funds overlay, and 2% guideline.
6. Hover over the chart for synchronized values; legend items are clickable to hide/show series.

## Computation Details

* YoY: 12‑month percent change.
* MoM: 1‑month percent change.
* SAAR: Annualized rate: $((1 + \text{MoM}/100)^{12} - 1) \times 100$.
* Index normalization: Each selected series rebased to 100 at first valid value inside the selected window.
* Smoothing: Centered rolling mean not used; simple trailing rolling mean with `min_periods=1`.

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Sidebar asks for API key | `.env` missing or invalid key | Paste key in sidebar or add to `.env` and reload |
| "Missing FRED_API_KEY" error (older versions) | Legacy behavior | Update to latest code; or supply key in `.env` |
| Empty chart | No series selected | Pick at least one CPI/PCE series |
| Very spiky SAAR | No smoothing | Increase smoothing window (3–6) |
| Old data not updating | Cache still valid | Delete `data/cache_fred.csv` |
| API error / timeout | Network or FRED rate limit | Retry after a minute; ensure key is correct |

## Project Structure

```
inflation_panel_st.py   # Streamlit app
data/cache_fred.csv     # Cached FRED responses (auto‑generated)
requirements.txt        # Python dependencies
README.md               # Documentation
```

## Possible Enhancements

* Add more CPI component breakdowns (e.g., transportation, medical care)
* Export chart as PNG/CSV directly from UI
* Compare against Fed inflation projections
* Add automatic refresh button & cache age display
* Support for custom time ranges beyond 5 years

## License

This project is licensed under the **MIT License** (see `LICENSE`).

## Recession Shading Logic

Recession periods use the monthly `USREC` (0/1) series. Consecutive months with value > 0.5 are grouped into blocks and rendered as light gray vertical rectangles behind the main traces. The algorithm walks the boolean series, recording start when entering a recession and end when leaving; an unfinished block at the end extends to the latest date.

## Acknowledgments

Data courtesy of Federal Reserve Bank of St. Louis (FRED). Built with Streamlit, Matplotlib, Seaborn, Pandas, NumPy.

---
Feel free to open issues or submit pull requests with improvements.

<!-- Screenshot placeholder -->
<!-- ![Dashboard Preview](dashboard_screenshot.png) -->


