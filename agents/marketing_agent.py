from langchain_groq import ChatGroq

def run_marketing_agent(state: dict) -> dict:
    llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)
    segments = state["segments"]
    insights = state["behavior_insights"]
    prompt = f"Based on customer segments {segments} and insights:\n{insights}\nGenerate targeted marketing strategies and personalized messaging recommendations for each group."
    response = llm.invoke(prompt)
    return {"marketing_strategies": response.content}