# US Inflation Dashboard

This project is my panel for our group’s Python Dashboard Assignment.  
My focus was on **US inflation** — how it’s evolved over time, what’s driving it, and how it compares to the Fed’s 2% target.

The dashboard is fully interactive and updates live when users change the time range or inflation measure.  
It lets you switch between **headline CPI**, **core CPI**, and **PCE inflation**, with extra context from **Fed interest rates** and **recession periods**.

# How it works

- Data comes directly from the [FRED API](https://fred.stlouisfed.org/), which provides official US economic data.  
- The panel is built in **Python** using **Plotly Dash**, with **Pandas** for data cleaning and **requests/python-dotenv** to securely use the API key.  
- When you change the date range, the graph updates automatically — so it’s a dynamic, live dashboard.
  
# What I learned

Building this helped me understand:
- How to connect to an API (FRED) and manage access keys using a `.env` file  
- How to use **Plotly Dash** to make interactive charts  
- How to structure a project in GitHub with a clean layout and `.gitignore`  
- How to troubleshoot layout bugs and data issues when working with live updates

It also helped me get more comfortable with GitHub — committing, pushing, and managing files properly.

# How to run it locally

1. **Clone this repository**  
   ```bash
   git clone https://github.com/gracegunne/US_Inflation_Dashboard.git
   cd US_Inflation_Dashboard

![Dashboard Preview](dashboard_screenshot.png)


