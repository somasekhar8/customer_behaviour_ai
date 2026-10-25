def run_segmentation_agent(state: dict) -> dict:

    segments = {
        "High-Value Champions": "Frequent buyers, high spend",
        "At-Risk Customers": "Declining visit frequency, high churn probability",
        "Bargain Hunters": "High discount sensitivity"  
    }
    return {"segments": segments}