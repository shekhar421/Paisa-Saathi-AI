import pandas as pd
import matplotlib.pyplot as plt


class GraphingAgent:
    """Builds the earnings and growth charts used by streamlit_app/app.py."""

    def _plot_series(self, data, value_col, title, ylabel):
        if not data:
            return None
        fig, ax = plt.subplots(figsize=(10, 5))
        for symbol, df in data.items():
            if df is None or df.empty or value_col not in df.columns:
                continue
            work = df.copy()
            work["Year"] = pd.to_numeric(work["Year"], errors="coerce")
            work[value_col] = pd.to_numeric(work[value_col], errors="coerce")
            work = work.dropna(subset=["Year", value_col]).sort_values("Year")
            hist = work[work.get("Type", "Historical") == "Historical"] if "Type" in work else work
            pred = work[work.get("Type", "") == "Predicted"] if "Type" in work else pd.DataFrame()
            if not hist.empty:
                ax.plot(hist["Year"], hist[value_col], marker="o", label=f"{symbol} actual")
            if not pred.empty:
                ax.plot(pred["Year"], pred[value_col], marker="s", linestyle="--", label=f"{symbol} forecast")
        ax.set_title(title)
        ax.set_xlabel("Year")
        ax.set_ylabel(ylabel)
        ax.grid(True, alpha=0.25)
        ax.legend(loc="best")
        fig.tight_layout()
        return fig

    def create_yearly_earnings_comparison(self, earnings_data_dict, title="Yearly Earnings"):
        return self._plot_series(earnings_data_dict, "Earnings", title, "Earnings")

    def create_growth_trend_comparison(self, growth_data_dict, title="Growth Trends"):
        return self._plot_series(growth_data_dict, "Growth_Rate", title, "Growth (%)")

    def create_combined_earnings_and_growth(self, earnings_data_dict, growth_data_dict,
                                           title="Earnings and Growth"):
        fig, axes = plt.subplots(2, 1, figsize=(10, 8))
        for data, col, ax, ylabel in [
            (earnings_data_dict, "Earnings", axes[0], "Earnings"),
            (growth_data_dict, "Growth_Rate", axes[1], "Growth (%)"),
        ]:
            for symbol, df in (data or {}).items():
                if df is None or df.empty or col not in df.columns:
                    continue
                work = df.copy()
                work["Year"] = pd.to_numeric(work["Year"], errors="coerce")
                work[col] = pd.to_numeric(work[col], errors="coerce")
                work = work.dropna(subset=["Year", col]).sort_values("Year")
                hist = work[work["Type"] == "Historical"] if "Type" in work else work
                pred = work[work["Type"] == "Predicted"] if "Type" in work else pd.DataFrame()
                if not hist.empty:
                    ax.plot(hist["Year"], hist[col], marker="o", label=f"{symbol} actual")
                if not pred.empty:
                    ax.plot(pred["Year"], pred[col], marker="s", linestyle="--", label=f"{symbol} forecast")
            ax.set_ylabel(ylabel)
            ax.grid(True, alpha=0.25)
            ax.legend(loc="best")
        axes[0].set_title(title)
        axes[1].set_xlabel("Year")
        fig.tight_layout()
        return fig

    def create_comparison_table(self, selected_symbols, earnings_data_dict, growth_data_dict):
        rows = []
        for symbol in selected_symbols:
            e = (earnings_data_dict or {}).get(symbol)
            g = (growth_data_dict or {}).get(symbol)
            latest_earnings = None
            forecast_earnings = None
            latest_growth = None
            forecast_growth = None
            if e is not None and not e.empty:
                if "Type" in e:
                    actual = e[e["Type"] == "Historical"]
                    forecast = e[e["Type"] == "Predicted"]
                else:
                    actual, forecast = e, pd.DataFrame()
                if not actual.empty:
                    latest_earnings = actual.sort_values("Year").iloc[-1]["Earnings"]
                if not forecast.empty:
                    forecast_earnings = forecast.sort_values("Year").iloc[0]["Earnings"]
            if g is not None and not g.empty:
                actual = g[g["Type"] == "Historical"] if "Type" in g else g
                forecast = g[g["Type"] == "Predicted"] if "Type" in g else pd.DataFrame()
                if not actual.empty:
                    latest_growth = actual.sort_values("Year").iloc[-1]["Growth_Rate"]
                if not forecast.empty:
                    forecast_growth = forecast.sort_values("Year").iloc[0]["Growth_Rate"]
            rows.append({
                "Symbol": symbol,
                "Latest Earnings": latest_earnings,
                "Next Forecast Earnings": forecast_earnings,
                "Latest Growth (%)": latest_growth,
                "Next Forecast Growth (%)": forecast_growth,
            })
        return pd.DataFrame(rows)
