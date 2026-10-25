import pandas as pd
def clean_customer_data(df: pd.DataFrame):
    df = df.dropna()
    summary = {
        "total_customers": len(df),
        "columns": list(df.columns),
        "mean_spend": float(df["total_spend"].mean()) if "total_spend" in df.columns else None

    }
    return df, summary