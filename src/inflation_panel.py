from dash import html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd

from data_fred import load_fred_cache
from transforms import yoy, mom, saar, normalize_100, roll3

def layout():
    return html.Div([
        html.Div([
            dcc.Dropdown(
                id="inflation-series",
                options=[
                    {"label": "Headline CPI", "value": "CPIAUCSL"},
                    {"label": "Core CPI", "value": "CPILFESL"},
                    {"label": "PCE Price Index", "value": "PCEPI"},
                ],
                value=["CPIAUCSL", "CPILFESL"], multi=True, clearable=False
            ),
            dcc.RadioItems(
                id="inflation-view",
                options=["YoY %", "MoM %", "MoM SAAR", "Index"],
                value="YoY %", inline=True
            ),
            dcc.RadioItems(
                id="inflation-range",
                options=["1Y", "3Y", "5Y", "10Y", "Max"],
                value="5Y", inline=True
            ),
            dcc.Checklist(
                id="inflation-toggles",
                options=["3-month avg", "2% guide", "Recessions", "Fed Funds"],
                value=["2% guide", "Recessions"], inline=True
            ),
        ], style={"display": "grid", "gap": "0.5rem"}),

        dcc.Graph(id="inflation-graph"),
        html.Div(id="inflation-cards", style={"marginTop": "0.5rem", "fontWeight": "500"})
    ], className="p-2")

def register_callbacks(app):
    df_full = load_fred_cache().sort_index()

    @app.callback(
        Output("inflation-graph", "figure"),
        Output("inflation-cards", "children"),
        Input("inflation-series", "value"),
        Input("inflation-view", "value"),
        Input("inflation-range", "value"),
        Input("inflation-toggles", "value"),
    )
    def update(series_list, view, rng, toggles):
        df = df_full.copy()
        look = {"1Y":12, "3Y":36, "5Y":60, "10Y":120}.get(rng)
        if look:
            df = df.iloc[-look:]
        series_to_plot = ["CPIAUCSL", "CPILFESL", "PCEPI"]
        if view == "YoY %":
            for s in series_to_plot: df[s] = yoy(df[s])
            y_title = "Percent, YoY"
        elif view == "MoM %":
            for s in series_to_plot: df[s] = mom(df[s])
            y_title = "Percent, MoM (SA)"
        elif view == "MoM SAAR":
            for s in series_to_plot: df[s] = saar(df[s])
            y_title = "Percent, SAAR"
        else:
            for s in series_to_plot: df[s] = normalize_100(df[s])
            y_title = "Index (Start = 100)"
        if "3-month avg" in toggles and view != "Index":
            for s in series_to_plot: df[s] = roll3(df[s])
        fig = go.Figure()
        for s in series_list:
            fig.add_scatter(x=df.index, y=df[s], mode="lines", name=s)
        if "2% guide" in toggles and view in {"YoY %", "MoM SAAR"}:
            fig.add_hline(y=2, line_dash="dot", opacity=0.5)
        if "Recessions" in toggles:
            rec = df["USREC"].fillna(0)
            blocks = (rec.diff().fillna(0) == 1).cumsum()
            for _, seg in df[rec == 1].groupby(blocks):
                fig.add_vrect(x0=seg.index.min(), x1=seg.index.max(),
                              fillcolor="grey", opacity=0.15, layer="below", line_width=0)
        if "Fed Funds" in toggles:
            fig.add_scatter(x=df.index, y=df["FEDFUNDS"], mode="lines",
                            name="Fed Funds", yaxis="y2")
            fig.update_layout(yaxis2=dict(overlaying="y", side="right", title="Fed Funds (%)", showgrid=False))
        fig.update_layout(margin=dict(t=20, r=10, b=20, l=10),
                          yaxis_title=y_title, legend_title="Series", hovermode="x unified")
        last_yoy = yoy(df_full["CPIAUCSL"]).iloc[-1]
        last_core = yoy(df_full["CPILFESL"]).iloc[-1]
        last_breakeven = df_full["T5YIE"].iloc[-1]
        cards = f"Current YoY CPI: {last_yoy:.1f}% | Core CPI: {last_core:.1f}% | 5y Breakeven: {last_breakeven:.2f}%"
        return fig, cards
