import numpy as np
import pandas as pd


class PredictionAgent:
    """Small, deterministic trend forecaster for yearly earnings data."""

    def _clean(self, df):
        if df is None or df.empty or not {"Year", "Earnings"}.issubset(df.columns):
            return pd.DataFrame(columns=["Year", "Earnings"])
        out = df[["Year", "Earnings"]].copy()
        out["Year"] = pd.to_numeric(out["Year"], errors="coerce")
        out["Earnings"] = pd.to_numeric(out["Earnings"], errors="coerce")
        out = out.dropna().sort_values("Year").drop_duplicates("Year")
        return out

    def _forecast(self, x, y, future_x):
        if len(x) == 0:
            return np.zeros(len(future_x), dtype=float)
        if len(x) == 1:
            return np.repeat(float(y[-1]), len(future_x))
        degree = min(2, len(x) - 1)
        coeffs = np.polyfit(x, y, degree)
        return np.polyval(coeffs, future_x)

    def predict_earnings(self, earnings_df, symbol, years_to_predict=2):
        hist = self._clean(earnings_df)
        if hist.empty:
            return None
        x = hist["Year"].to_numpy(dtype=float)
        y = hist["Earnings"].to_numpy(dtype=float)
        last_year = int(max(x))
        future_years = np.arange(last_year + 1, last_year + max(1, years_to_predict) + 1)
        future_values = self._forecast(x, y, future_years.astype(float))
        historical = hist.assign(Type="Historical", Symbol=symbol)
        predicted = pd.DataFrame({
            "Year": future_years,
            "Earnings": future_values,
            "Type": "Predicted",
            "Symbol": symbol,
        })
        return pd.concat([historical, predicted], ignore_index=True)

    def predict_growth_rate(self, earnings_df, symbol, years_to_predict=2):
        hist = self._clean(earnings_df)
        if len(hist) < 2:
            return None
        hist = hist.copy()
        hist["Growth_Rate"] = hist["Earnings"].pct_change() * 100.0
        hist = hist.dropna(subset=["Growth_Rate"])
        if hist.empty:
            return None
        x = hist["Year"].to_numpy(dtype=float)
        y = hist["Growth_Rate"].to_numpy(dtype=float)
        last_year = int(max(x))
        future_years = np.arange(last_year + 1, last_year + max(1, years_to_predict) + 1)
        future_values = self._forecast(x, y, future_years.astype(float))
        historical = hist[["Year", "Growth_Rate"]].assign(Type="Historical", Symbol=symbol)
        predicted = pd.DataFrame({
            "Year": future_years,
            "Growth_Rate": future_values,
            "Type": "Predicted",
            "Symbol": symbol,
        })
        return pd.concat([historical, predicted], ignore_index=True)
