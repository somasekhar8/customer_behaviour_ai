import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv(override=True)

def run_analysis_agent(state: dict) -> dict:

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.2,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    summary = state["cleaned_data_summary"]

    prompt = f"""
You are an expert Customer Behavior Analyst.

Analyze the following customer dataset summary:

{summary}

Generate a clear, professional, data-driven analysis.

Follow this exact structure:

## 1. Customer Overview
Explain the total customers, transactions,
revenue and average spending.

## 2. Purchasing Behavior
Identify:
- High-spending customers
- Frequently purchased products
- Customer purchase patterns

## 3. Customer Engagement
Explain customer activity based on
purchase frequency and available dates.

## 4. Churn Risk
Identify potential inactive customers
only when sufficient historical data exists.

Do not invent churn percentages.

## 5. Key Business Insights
Provide 3-5 meaningful insights supported
by the dataset.

Rules:
- Use simple professional English.
- Avoid generic explanations.
- Include actual numbers when available.
- Never invent missing metrics.
- If data is missing, clearly mention it.
- Do not include unnecessary technical metadata.
    """

    response = llm.invoke(prompt)

    return {
        "behavior_insights": response.content
    }