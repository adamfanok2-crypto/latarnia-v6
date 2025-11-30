"""
Latarnia Web UI Module

Streamlit-based web interface for the Latarnia AI framework.
"""

import streamlit as st
from latarnia.core.logic import LatarniaCore


def main():
    """Main entry point for the Latarnia Web UI."""
    st.set_page_config(
        page_title="Latarnia v6",
        page_icon="🏠",
        layout="wide"
    )
    
    st.title("🏠 Latarnia v6")
    st.subheader("An Ethical Reasoning Framework for AI Systems")
    
    # Initialize the core engine
    core = LatarniaCore()
    
    # Sidebar
    with st.sidebar:
        st.header("About")
        st.write(f"Version: {core.version}")
        st.write("Latarnia provides ethical decision-making, fact auditing, "
                 "consequence simulation, and neutral mediation.")
    
    # Main content
    st.markdown("---")
    
    # Input section
    st.header("Process Input")
    user_input = st.text_area(
        "Enter your query or statement:",
        placeholder="Type something to process through the ethical reasoning framework..."
    )
    
    if st.button("Process", type="primary"):
        if user_input:
            with st.spinner("Processing through ethical reasoning framework..."):
                result = core.process(user_input)
            
            st.success("Processing complete!")
            st.json(result)
        else:
            st.warning("Please enter some input to process.")
    
    st.markdown("---")
    
    # Features section
    st.header("Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🔍 Fact Auditing")
        st.write("Verify and validate facts for accuracy and consistency.")
    
    with col2:
        st.subheader("⚡ Consequence Simulation")
        st.write("Simulate potential outcomes of actions before execution.")
    
    with col3:
        st.subheader("⚖️ Neutral Mediation")
        st.write("Provide balanced analysis while preserving user sovereignty.")
    
    # Footer
    st.markdown("---")
    st.caption("Latarnia v6 - Ethical AI Framework | MIT License")


if __name__ == "__main__":
    main()
