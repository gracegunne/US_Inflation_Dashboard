# Run with: python app.py
import os, sys
from dash import Dash, html
sys.path.append("src")

from inflation_panel import layout as inflation_layout, register_callbacks as inflation_callbacks

app = Dash(__name__, title="US Macro Dashboard – Inflation")
app.layout = html.Div([
    html.H2("US Inflation Panel (CPI / Core / PCE)"),
    inflation_layout()
], className="p-4")

inflation_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
