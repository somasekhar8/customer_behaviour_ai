from typing import TypedDict, Dict, Any, List
from langgraph.graph import StateGraph, END
from agents.data_agent import run_data_agent
from agents.analysis_agent import run_analysis_agent
from agents.segmentation_agent import run_segmentation_agent
from agents.prediction_agent import run_prediction_agent
from agents.marketing_agent import run_marketing_agent
from agents.report_agent import run_report_agent

class AgentState(TypedDict):
    raw_data_path: str
    cleaned_data_summary: Dict[str, Any]
    behavior_insights: str
    segments: Dict[str, Any]
    predictions: Dict[str, Any]
    marketing_strategies: str
    final_report: str

def build_customer_behavior_graph():
    workflow = StateGraph(AgentState)

    # Define Nodes
    workflow.add_node("data_agent", run_data_agent)
    workflow.add_node("analysis_agent", run_analysis_agent)
    workflow.add_node("segmentation_agent", run_segmentation_agent)
    workflow.add_node("prediction_agent", run_prediction_agent)
    workflow.add_node("marketing_agent", run_marketing_agent)
    workflow.add_node("report_agent", run_report_agent)

    # Define Edges
    workflow.set_entry_point("data_agent")
    workflow.add_edge("data_agent", "analysis_agent")
    workflow.add_edge("analysis_agent", "segmentation_agent")
    workflow.add_edge("segmentation_agent", "prediction_agent")
    workflow.add_edge("prediction_agent", "marketing_agent")
    workflow.add_edge("marketing_agent", "report_agent")
    workflow.add_edge("report_agent", END)

    return workflow.compile()