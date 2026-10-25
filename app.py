import os
import streamlit as st
from dotenv import load_dotenv
from workflows.graph import build_customer_behavior_graph

# 1. Load environment variables from .env file
load_dotenv()

st.set_page_config(page_title="Customer Behavior AI", layout="wide")
st.title("Customer Behavior AI Workflow")

# 2. Sidebar API Key configuration
st.sidebar.header("Configuration")
env_api_key = os.getenv("GOOGLE_API_KEY", "")

api_key = st.sidebar.text_input(
    "GOOGLE API Key",
    value=env_api_key,
    type="password",
    help="Loaded from .env by default. You can paste a key here to override."
)

if not api_key:
    st.warning("Please provide an OpenAI API Key in the sidebar or set OPENAI_API_KEY in your .env file to proceed.")
else:
    # Set the key in environment variables so LangChain agents pick it up globally
    os.environ["GOOGLE_API_KEY"] = api_key

# 3. Main Application Flow
uploaded_file = st.file_uploader("Upload Customer Dataset (CSV)", type=["csv"])

if uploaded_file:
    data_path = f"data/{uploaded_file.name}"
    os.makedirs("data", exist_ok=True)
    
    with open(data_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File uploaded successfully: `{uploaded_file.name}`")

    if st.button("Run Multi-Agent Analysis", type="primary"):
        if not api_key:
            st.error("Cannot run analysis without an GEMINI API Key.")
        else:
            with st.spinner("Executing Multi-Agent Workflow..."):
                try:
                    graph = build_customer_behavior_graph()
                    initial_state = {"raw_data_path": data_path}
                    
                    # Run the graph workflow
                    result = graph.invoke(initial_state)

                    st.header("Executive Summary Report")
                    st.markdown(result.get("final_report", "No report generated."))
                    
                    with st.expander("Detailed Marketing Strategies"):
                        st.markdown(result.get("marketing_strategies", "No strategies generated."))

                    with st.expander("Raw Behavioral Insights & Predictions"):
                        st.subheader("Customer Segments")
                        st.json(result.get("segments", {}))
                        
                        st.subheader("Predictions")
                        st.json(result.get("predictions", {}))

                except Exception as e:
                    st.error(f"An error occurred while running the workflow: {str(e)}")