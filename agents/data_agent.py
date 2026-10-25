import pandas as pd
from utils.data_preprocessing import clean_customer_data

def run_data_agent(state: dict) -> dict:
    df = pd.read_csv(state["raw_data_path"])
    cleaned_df, summary = clean_customer_data(df)
    return {"cleaned_data_summary": summary}