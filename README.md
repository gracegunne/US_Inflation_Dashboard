# US Inflation DashboardUS Inflation Dashboard# US Inflation Dashboard<div align="center">



Quick way to visualize US inflation trends over the past 5 years using different CPI measures and the PCE index.



## What it doesQuick way to visualize US inflation trends over the past 5 years using different CPI measures and the PCE index.



Track 6 different inflation metrics - headline CPI, core CPI, PCE, energy, food, and housing. You can view them as year-over-year percentages, month-over-month changes, or annualized rates. Also shows the Fed policy rate and recession periods for context.



Data comes from FRED and gets cached for 24 hours so you're not constantly hitting their API.What it doesQuick way to visualize US inflation trends over the past 5 years using different CPI measures and the PCE index.<h1>US Inflation Dashboard (5Y)</h1>



## Features



### Inflation MetricsTrack 6 different inflation metrics - headline CPI, core CPI, PCE, energy, food, and housing. You can view them as year-over-year percentages, month-over-month changes, or annualized rates. Also shows the Fed policy rate and recession periods for context.<em>Interactive exploration of US inflation dynamics across 6 key inflation metrics with recession shading and Fed policy context.</em>

Six inflation measures to choose from: CPI Headline, Core CPI (minus food and energy), PCE Price Index, CPI Energy, CPI Food, and CPI Housing



### Display Options

- Always shows the last 5 years of dataData comes from FRED and gets cached for 24 hours so you're not constantly hitting their API.## What it does

- View as year-over-year percentage, month-over-month percentage, annualized rate, or indexed to 100

- Line charts, bar charts, or both

- Optional 3-month smoothing to reduce noise

Features</div>

### Additional Overlays

- Recession shading using NBER data

- Fed Funds Rate overlay

- 2 percent guideline toggleSix inflation measures to choose from: CPI Headline, Core CPI (minus food and energy), PCE Price Index, CPI Energy, CPI Food, and CPI HousingTrack 6 different inflation metrics (headline CPI, core CPI, PCE, energy, food, and housing) with options to view year-over-year, month-over-month, or annualized rates. Also shows Fed policy rate and recession periods for context.



## Data Sources



All data from FRED:Always shows the last 5 years of data## Overview



- CPIAUCSL - Headline CPI

- CPILFESL - Core CPI (no food or energy)

- PCEPI - PCE Price Index (what the Fed actually watches)View as year-over-year percentage, month-over-month percentage, annualized rate, or indexed to 100Data comes from FRED and gets cached for 24 hours so you're not constantly hitting their API.

- CPIENGSL - CPI Energy

- CPIUFDSL - CPI Food

- CPIHOSNS - CPI Housing

- FEDFUNDS - Fed Funds RateLine charts, bar charts, or bothThis Streamlit app lets you explore US inflation across 6 comprehensive measures over a 5-year time horizon. You can quickly switch among CPI (headline, core, energy, food, housing) and PCE price index, view growth rates (YoY, MoM, SAAR) or level indices, apply smoothing, and overlay macro context (Fed Funds Rate, NBER recession periods, 2% guide line).

- USREC - Recession indicator



## Setup

Optional 3-month smoothing to reduce noise## Features

### Requirements

You need Python 3.9 or higher and a free FRED API key from https://fred.stlouisfed.org/



### Installation StepsRecession shading using NBER dataAll data are pulled on demand from the Federal Reserve Economic Data (FRED) API and cached locally for 24 hours to minimize API calls.



Clone the repo:

```

git clone https://github.com/gracegunne/US_Inflation_Dashboard.gitFed Funds Rate overlay- 6 inflation measures: CPI Headline, Core CPI (minus food & energy), PCE Price Index, CPI Energy, CPI Food, CPI Housing

cd US_Inflation_Dashboard

```



Optional - create a virtual environment:2 percent guideline toggle- Shows last 5 years of data## Why it’s interesting

```

python -m venv .venv

.venv\Scripts\Activate.ps1

```Data Sources- View as YoY %, MoM %, annualized rate, or indexed to 100



Install the packages:

```

pip install -r requirements.txtAll data from FRED:- Line charts, bar charts, or bothThis dashboard makes it easy to answer practical macro questions:

```



Add your FRED key:

```CPIAUCSL - Headline CPI- Optional 3-month smoothing- Are inflation trends accelerating or cooling right now (MoM vs SAAR)?

echo FRED_API_KEY=YOUR_KEY_HERE > .env

```CPILFESL - Core CPI (no food or energy)



Run it:PCEPI - PCE Price Index (what the Fed actually watches)- Recession shading (NBER data)- How do different inflation components (energy, food, housing, core) compare?

```

streamlit run inflation_panel_st.pyCPIENGSL - CPI Energy

```

CPIUFDSL - CPI Food- Fed Funds Rate overlay- Is inflation above/below the 2% guide line—and for how long?

Open the local URL, usually http://localhost:8501

CPIHOSNS - CPI Housing

## How to use

FEDFUNDS - Fed Funds Rate- 2% guideline toggle- How does inflation typically move around recessions and policy tightening?

### Basic Steps

1. Pick an inflation metric from the dropdownUSREC - Recession indicator

2. Choose how you want to view it - year-over-year, month-over-month, annualized, or index

3. Turn on smoothing if the chart looks too noisy

4. Toggle recession shading, Fed rate, and 2 percent line as needed

Setup

### Data Caching

The cache file saves data for 24 hours. Delete data/cache_fred.csv if you need fresh data.## Data Sources## Features



## TroubleshootingYou need Python 3.9 or higher and a free FRED API key from https://fred.stlouisfed.org/



### Common Issues



**App asks for API key** - Either paste it in the sidebar or add it to a .env fileClone the repo:



**Chart is empty** - Make sure you selected a seriesgit clone https://github.com/gracegunne/US_Inflation_Dashboard.gitAll data from FRED:* **6 comprehensive inflation metrics**: CPI Headline, CPI Core (ex Food & Energy), PCE Price Index, CPI Energy, CPI Food, CPI Housing



**SAAR looks crazy** - Turn on smoothingcd US_Inflation_Dashboard



**Data seems old** - Delete data/cache_fred.csv to refresh* Always displays last 5 years of data



## What's includedOptional - create a virtual environment:



- inflation_panel_st.py - main apppython -m venv .venv- `CPIAUCSL` - Headline CPI* Multiple view transformations: YoY %, MoM %, annualized SAAR %, or Index (rebased to 100 at window start)

- data/cache_fred.csv - cached data (auto-generated)

- requirements.txt - dependencies.venv\Scripts\Activate.ps1

- README.md - this file

- `CPILFESL` - Core CPI (no food/energy)* Plot types: Lines, Bars, or hybrid Lines + Bars

## Ideas for later

Install the packages:

- Add more CPI components like transportation and medical

- Export charts directlypip install -r requirements.txt- `PCEPI` - PCE Price Index (what the Fed actually watches)* Optional 3-month smoothing to reduce noise

- Compare to Fed projections

- Show cache age

- Custom date ranges

Add your FRED key:- `CPIENGSL` - CPI Energy* Recession shading using NBER recession indicator (USREC)

---

echo FRED_API_KEY=YOUR_KEY_HERE > .env

Data from Federal Reserve Bank of St. Louis (FRED). Built with Streamlit and the usual Python data stack.

- `CPIUFDSL` - CPI Food* Fed Funds Rate overlay with dual y‑axis

Run it:

streamlit run inflation_panel_st.py- `CPIHOSNS` - CPI Housing* 2% guide line (or 100 for index normalization) toggle



Open the local URL, usually http://localhost:8501- `FEDFUNDS` - Fed Funds Rate* Lightweight, fast UI powered by Streamlit & Matplotlib/Seaborn



How to use- `USREC` - Recession indicator



Pick an inflation metric from the dropdown## Data Sources (FRED Series)



Choose how you want to view it - year-over-year, month-over-month, annualized, or index## Setup



Turn on smoothing if the chart looks too noisy| Purpose | Series ID | Description |



Toggle recession shading, Fed rate, and 2 percent line as neededYou need Python 3.9+ and a free FRED API key from https://fred.stlouisfed.org/|---------|-----------|-------------|



The cache file saves data for 24 hours. Delete data/cache_fred.csv if you need fresh data.| Headline CPI | `CPIAUCSL` | Consumer Price Index for All Urban Consumers |



Troubleshooting```bash| Core CPI | `CPILFESL` | CPI less Food & Energy |



App asks for API key - Either paste it in the sidebar or add it to a .env filegit clone https://github.com/gracegunne/US_Inflation_Dashboard.git| PCE Price Index | `PCEPI` | Personal Consumption Expenditures Price Index (Fed's preferred measure) |



Chart is empty - Make sure you selected a seriescd US_Inflation_Dashboard| CPI Energy | `CPIENGSL` | Energy component of CPI |



SAAR looks crazy - Turn on smoothing| CPI Food | `CPIUFDSL` | Food component of CPI |



Data seems old - Delete data/cache_fred.csv to refresh# optional: virtual environment| CPI Housing | `CPIHOSNS` | Housing component of CPI |



What's includedpython -m venv .venv| Policy Rate | `FEDFUNDS` | Effective Federal Funds Rate |



inflation_panel_st.py - main app.venv\Scripts\Activate.ps1| Recession Indicator | `USREC` | NBER recession periods (0/1) |

data/cache_fred.csv - cached data (auto-generated)

requirements.txt - dependencies

README.md - this file

pip install -r requirements.txt## Requirements

Ideas for later



Add more CPI components like transportation and medical

Export charts directly# add your FRED key* Python 3.9+ (tested with 3.11)

Compare to Fed projections

Show cache ageecho "FRED_API_KEY=YOUR_KEY_HERE" > .env* FRED API key (free from https://fred.stlouisfed.org/)

Custom date ranges

* Packages listed in `requirements.txt`

Data from Federal Reserve Bank of St. Louis (FRED). Built with Streamlit and the usual Python data stack.

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


