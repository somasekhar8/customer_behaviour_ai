from langchain_groq import ChatGroq

def extract_text(response):
    content = response.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        return "\n".join(
            item.get("text", "")
            for item in content
            if isinstance(item, dict)
            and item.get("type") == "text"
        )

    return str(content)

def run_report_agent(state: dict) -> dict:
    llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.3)
    prompt = f"""Synthesize an executive summary report from:
- Insights: {state['behavior_insights']}
- Segments: {state['segments']}
- Predictions: {state['predictions']}
- Marketing Strategy: {state['marketing_strategies']}
"""
    response = llm.invoke(prompt)
    return {"report": extract_text(response)}